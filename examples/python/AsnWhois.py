"""Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.asnwhois_api import ASNWHOISApi

# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = ASNWHOISApi(ApiClient(config))

result = api.asn_whois(asn="AS15169")
print(result)
