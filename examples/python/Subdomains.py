"""Runnable example: Subdomains Lookup (GET /v1.0/subdomains)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.subdomains_api import SubdomainsApi

# Parameters for subdomains (GET /v1.0/subdomains):
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = SubdomainsApi(ApiClient(config))

result = api.subdomains(domain="example.com", after="2000-01-01", before=str(date.today()))
print(result)
