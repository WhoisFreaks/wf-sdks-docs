"""Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

result = api.whois_history(domain_name="example.com")
print(result)
