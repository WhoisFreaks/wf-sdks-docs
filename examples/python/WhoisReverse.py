"""Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_reverse_with_http_info(api_key="YOUR_API_KEY", keyword="value")
print("status:", resp.status_code)
print(resp.data)
