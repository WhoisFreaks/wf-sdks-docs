"""Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPWHOISApi(ApiClient(config))

resp = api.db_ip_whois_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
