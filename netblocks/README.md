# Netblocks

**This is not an official Google product.**

This module retrieves the DNS entries recursively as per the below links

    The GCE ranges
        https://cloud.google.com/compute/docs/faq#where_can_i_find_product_name_short_ip_ranges
    The Google Services ranges
        https://support.google.com/a/answer/60764
    The AWS ranges
        https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

Install the package with `pip install netblocks` or `pip install git+https://github.com/hm-distro/netblocks/`

The `fetch()` method has the default parameter value of `initial_dns_list=[GOOGLE_INITIAL_CLOUD_NETBLOCK_DNS, GOOGLE_INITIAL_SPF_NETBLOCK_DNS]`

where 

    #The GCE ranges
    GOOGLE_INITIAL_CLOUD_NETBLOCK_DNS = "_cloud-netblocks.googleusercontent.com"

    #The Google Services ranges
    GOOGLE_INITIAL_SPF_NETBLOCK_DNS= "_spf.google.com"

    #The AWS ranges
    AWS_IP_RANGES="https://ip-ranges.amazonaws.com/ip-ranges.json"

See [here](https://github.com/hm-distro/netblocks) on how to use this module in Google App Engine  
### API Usage

    import netblocks
    cidr_blocks = set()
    api = netblocks.NetBlocks()
    try:
        # returns both GOOGLE_INITIAL_CLOUD_NETBLOCK_DNS and GOOGLE_INITIAL_SPF_NETBLOCK_DNS
        cidr_blocks = api.fetch()
        
        # To get only the SPF list use the below:
        #  cidr_blocks = api.fetch([netblocks.GOOGLE_INITIAL_SPF_NETBLOCK_DNS])
 
        
        # To get only the GCE list use the below:
        #  cidr_blocks = api.fetch([netblocks.GOOGLE_INITIAL_CLOUD_NETBLOCK_DNS]) 
        
        # To get only the AWS list use the below:
        #  cidr_blocks = api.fetch([netblocks.AWS_IP_RANGES]) 
        
        """
        The cidr_blocks set contains strings like the below
        ip4:146.148.2.0/23
        ...
        ip6:2600:1900::/35
        """
        
    except netblocks.NetBlockRetrievalException as err:
        #exception handling
        pass

## Language
- [Python](https://www.python.org/)

## Dependencies
requests

## License
Apache 2.0; see [LICENSE](https://github.com/hm-distro/netblocks/blob/master/netblocks/LICENSE) for details.