#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module retrieves the DNS entries recursively as per the below link.

https://cloud.google.com/compute/docs/faq#where_can_i_find_short_product_name_ip_ranges
"""
import json
import logging
import time

import cloudstorage as gcs
import webapp2

import config
import netblocks


class DNSRefreshException(Exception):
    """
    This exception is a wrapper exception from this module.
    
    This exception is thrown for any non successful operation in getting
    the DNS entries
    """
    pass


class DNSRefresh(webapp2.RequestHandler):
    """
    This abstract class retrieves the DNS entries recursively.
  
    The implementing class needs to implement the process method
    to persist/process the CIDR blocks that are retrieved.
    """

    def process(self, cidr_blocks):  # pylint: disable=unused-argument,unused-variable
        """
        Abstract callback method that is called on the set of CIDR blocks.
    
        The inheriting class will need to implement this method and process
        the CIDR blocks.
    
        The set contains strings like the below
        ip4:146.148.2.0/23
        ip6:2600:1900::/35
    
        Args:
          cidr_blocks: The URL to fetch the json payload.
    
        Raises:
          DNSRefreshException: raised if any issue in dns refresh
    
        """
        raise NotImplementedError("Please Implement this method")

    def get(self):
        """
        The main entry point to this class.
    
        This method is the entry point that is called by the scheduler/cron.
        This method makes a call to the DNS servers, retrieves the json payload.
        extracts the ip addresses, and inserts them into a set that is returned.
    
        Returns:
          A set of cidr blocks
    
        """
        logging.info("dns refresh called")
        cidr_blocks = set()
        netblocks_api = netblocks.NetBlocks()

        try:

            cidr_blocks = netblocks_api.fetch()
            self.process(cidr_blocks)

        except netblocks.NetBlockRetrievalException as err:
            logging.error(err.message)
            self.response.headers["Content-Type"] = "text/plain"
            self.response.write(err.message)
            self.response.set_status(500)
            return

        self.response.headers["Content-Type"] = "text/plain"
        self.response.write(json.dumps(list(cidr_blocks)))


class UpdateGCSBucket(DNSRefresh):
    """
    This class writes the CIR ranges to a GCS bucket, as a text file.
  
    """

    def process(self, cidr_blocks):
        """
        Implementation of method that writes the cidr blocks to a GCS bucket.
    
        Args:
          cidr_blocks: The URL to fetch the json payload
    
        Raises:
          DNSRefreshException: raised if any issue in dns refresh
        """
        should_write_file = False
        fqdn_file_name = "/%s/%s" % (config.GCS_BUCKET, config.FILE_NAME)
        logging.info("Processing file at %s", fqdn_file_name)
        old_cidr_blocks = set()

        # Check if the file already exists.
        # If it does, read the file into old_cidr_blocks, to compare later
        try:
            gcs_current_file = gcs.open(fqdn_file_name, "r")
        except gcs.NotFoundError:
            should_write_file = True
        else:
            with gcs_current_file:
                for line in gcs_current_file:
                    old_cidr_blocks.add(line.strip())

        # check if there is any differences between current and old blocks
        if old_cidr_blocks != cidr_blocks:
            logging.info("Change detected")
            should_write_file = True

        if should_write_file:
            # Write the new file, if there is a change
            try:
                write_retry_params = gcs.RetryParams(backoff_factor=1.1)
                gcs_file = gcs.open(fqdn_file_name,
                                    "w",
                                    content_type="text/plain",
                                    options={
                                        "x-goog-meta-updated-time": str(time.time())
                                    },
                                    retry_params=write_retry_params)
            except Exception as e:  # pylint: disable=broad-except
                logging.error(e.message)
                raise DNSRefreshException(e.message)
            else:
                with gcs_file:
                    for item in cidr_blocks:
                        gcs_file.write(item + "\n")


APP = webapp2.WSGIApplication([
    ("/dns/refresh", UpdateGCSBucket),  # URL to be called by the cron
], debug=True)
