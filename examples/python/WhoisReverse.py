"""Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

result = api.whois_reverse(keyword="value")
print(result)
