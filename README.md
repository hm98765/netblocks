# Netblocks

**This is not an official Google product.**

This is a [Google App Engine](https://cloud.google.com/appengine/) app that regularly checks the DNS entries as described [here](https://cloud.google.com/compute/docs/faq#where_can_i_find_short_product_name_ip_ranges).
This code updates the GCS bucket, when there is a change in the CIDR blocks for GCE.

Downstream systems can hook into the Object notification on the [GCS bucket](https://cloud.google.com/storage/docs/object-change-notification) and accordingly
do something with the file, with the updated CIDR ranges.
The schedule of this refresh can be managed in the cron.yaml and the bucket and file where the CIDR ranges should be written to can be changed in the config.py

Potential listeners could be [Cloud Functions](https://cloud.google.com/functions/).

### API Usage

    import netblocks
    cidr_blocks = set()
    netblocks_api = netblocks.NetBlocks()
    try:
        cidr_blocks = netblocks_api.fetch()
        
        """
        The cidr_blocks set contains strings like the below
        ip4:146.148.2.0/23
        ...
        ip6:2600:1900::/35
        """
        
    except netblocks.NetBlockRetrievalException as err:
        #exception handling
        pass

### The GAE App
*  UpdateGCSBucket </br>

 This class creates a file in the GCS bucket as specified in config.py.<br/>
 The files contains entries such as the below: <br/>
 ip4:146.148.2.0/23<br/>
 ...<br/>
 ip6:2600:1900::/35<br/>
  <p style='color:red'>
 Make sure to create a bucket prior to runnign the app<br/>
 This bucket-name should be changed in the config.py under GCS_BUCKET
 </p>
 
 
## Products
- [Google App Engine](https://cloud.google.com/appengine/)

## Language
- [Python](https://www.python.org/)

## Dependencies
listed in the requirements.txt


## License
Apache 2.0; see [LICENSE](LICENSE) for details.
