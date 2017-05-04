# Netblocks

**This is not an official Google product.**

This is a [Google App Engine](https://cloud.google.com/appengine/) app that regularly checks the DNS entries as described [here](https://cloud.google.com/compute/docs/faq#where_can_i_find_short_product_name_ip_ranges).
This code updates the GCS bucket, when there is a change in the CIDR blocks for GCE.

Downstream systems can hook into the Object notification on the [GCS bucket](https://cloud.google.com/storage/docs/object-change-notification) and accordingly
do something with the file, with the updated CIDR ranges.
The schedule of this refresh can be managed in the cron.yaml and the bucket and file where the CIDR ranges should be written to can be changed in the config.py

Potential listeners could be [Cloud Functions](https://cloud.google.com/functions/).


## Products
- [Google App Engine](https://cloud.google.com/appengine/)

## Language
- [Python](https://www.python.org/)

## Dependencies
run the below commands in the current directory <br/>
The required libraries will be installed into ./lib <br/>
mkdir lib <br/>
pip install -t ./lib/ GoogleAppEngineCloudStorageClient <br/>



## License
Apache 2.0; see [LICENSE.txt](LICENSE.txt) for details.
