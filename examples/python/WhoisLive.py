"""Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)
