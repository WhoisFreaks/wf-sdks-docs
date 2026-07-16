"""Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DNSApi(ApiClient(config))

result = api.dns_historical(domain_name="example.com", var_type="value")
print(result)
