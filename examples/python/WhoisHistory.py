"""Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_history_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)
