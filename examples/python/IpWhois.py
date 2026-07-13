"""Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ipwhois_api import IPWHOISApi

# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = IPWHOISApi(ApiClient(config))

resp = api.ip_whois_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)
