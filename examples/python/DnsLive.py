"""Runnable example: Live DNS Lookup (GET /v2.0/dns/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsLive (GET /v2.0/dns/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", ip_address="8.8.8.8", var_type="value")
print("status:", resp.status_code)
print(resp.data)
