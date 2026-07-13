"""Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_reverse_with_http_info(api_key="YOUR_API_KEY", value="value", var_type="a", exact=True)
print("status:", resp.status_code)
print(resp.data)
