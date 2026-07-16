"""Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DNSApi(ApiClient(config))

result = api.dns_reverse(value="value", var_type="a", exact=True)
print(result)
