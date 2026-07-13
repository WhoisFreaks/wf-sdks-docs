"""Runnable example: Subdomains Lookup (GET /v1.0/subdomains)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.subdomains_api import SubdomainsApi

# Parameters for subdomains (GET /v1.0/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = SubdomainsApi(ApiClient(config))

resp = api.subdomains_with_http_info(api_key="YOUR_API_KEY", domain="example.com", after="2000-01-01", before=str(date.today()))
print("status:", resp.status_code)
print(resp.data)
