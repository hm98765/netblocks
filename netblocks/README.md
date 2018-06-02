# Netblocks

**This is not an official Google product.**

This module retrieves the DNS entries recursively as per the below links

https://cloud.google.com/compute/docs/faq#where_can_i_find_short_product_name_ip_ranges
https://support.google.com/a/answer/60764

Install the package with `pip install git+https://github.com/hm-distro/netblocks/`

The `fetch()` method has the default parameter value of `initial_dns_list=[INITIAL_CLOUD_NETBLOCK_DNS, INITIAL_SPF_NETBLOCK_DNS]`

where 


INITIAL_CLOUD_NETBLOCK_DNS = "_cloud-netblocks.googleusercontent.com"

INITIAL_SPF_NETBLOCK_DNS= "_spf.google.com"

### API Usage

    import netblocks
    cidr_blocks = set()
    netblocks_api = netblocks.NetBlocks()
    try:
        # returns both INITIAL_CLOUD_NETBLOCK_DNS and INITIAL_SPF_NETBLOCK_DNS
        cidr_blocks = netblocks_api.fetch()
        
        # To get only the SPF list use the below:
        #  cidr_blocks = api.fetch([netblocks.INITIAL_SPF_NETBLOCK_DNS])
 
        
        # To get only the GCE list use the below:
        #  cidr_blocks = api.fetch([netblocks.INITIAL_CLOUD_NETBLOCK_DNS]) 
        
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
Apache 2.0; see [LICENSE](LICENSE) for details.
