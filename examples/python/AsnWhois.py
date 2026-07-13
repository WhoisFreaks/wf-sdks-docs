"""Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.asnwhois_api import ASNWHOISApi

# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = ASNWHOISApi(ApiClient(config))

resp = api.asn_whois_with_http_info(api_key="YOUR_API_KEY", asn="AS15169")
print("status:", resp.status_code)
print(resp.data)
