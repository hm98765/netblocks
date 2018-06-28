# Netblocks

**This is not an official Google product.**

This is a [Google App Engine](https://cloud.google.com/appengine/) app that regularly checks the DNS entries using the [netblocks](https://github.com/hm-distro/netblocks/blob/master/netblocks/README.md) module.
This App engine code updates the GCS bucket, when there is a change in the CIDR blocks for GCE.

The netblocks api module itself can be used outside App Engine.
Install the package with `pip install netblocks` or `pip install git+https://github.com/hm-distro/netblocks/`
    
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
 Make sure to create a bucket prior to deploying the app<br/>
 This bucket-name should be changed in the config.py under GCS_BUCKET
 
 Deploy using 
 
 `gcloud app  deploy app.yaml`
 
 `gcloud app  deploy cron.yaml`
 
  
 
## Products
- [Google App Engine](https://cloud.google.com/appengine/)

## Language
- [Python](https://www.python.org/)

## Dependencies
Run these steps before deploying the app <br/>
mkdir lib <br/>
pip install -t ./lib/ google-api-python-client <br/>
pip install -t ./lib/ GoogleAppEngineCloudStorageClient <br/> 
pip install -t ./lib/ requests <br/>
pip install -t ./lib/ oauth2client <br/> 
pip install -t ./lib/ requests-toolbelt <br/>

## License
Apache 2.0; see [LICENSE](LICENSE) for details.
