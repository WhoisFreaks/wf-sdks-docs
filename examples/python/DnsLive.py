"""Runnable example: Live DNS Lookup (GET /v2.0/dns/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsLive (GET /v2.0/dns/live):
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DNSApi(ApiClient(config))

result = api.dns_live(domain_name="example.com", ip_address="8.8.8.8", var_type="value")
print(result)
