"""Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_historical_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", var_type="value")
print("status:", resp.status_code)
print(resp.data)
