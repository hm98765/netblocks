# Netblocks

**This is not an official Google product.**
This module retrieves the DNS entries recursively as per the below links

https://cloud.google.com/compute/docs/faq#where_can_i_find_short_product_name_ip_ranges
https://support.google.com/a/answer/60764

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

## Language
- [Python](https://www.python.org/)

## Dependencies
requests

## License
Apache 2.0; see [LICENSE](LICENSE) for details.
