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
This is the main GAE class.

Nothing much is happening here, as the app primarily is based on the GAE cron.
"""
import webapp2


class MainPage(webapp2.RequestHandler):
    """
    Main class for serving web traffic.
    
    Nothing much is done right now.
    """

    def get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("OK")


APP = webapp2.WSGIApplication([
    ("/", MainPage),  # Show a default main page
], debug=True)
