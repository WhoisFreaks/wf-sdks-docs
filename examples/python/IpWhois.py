"""Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ipwhois_api import IPWHOISApi

# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPWHOISApi(ApiClient(config))

result = api.ip_whois(ip="8.8.8.8")
print(result)
