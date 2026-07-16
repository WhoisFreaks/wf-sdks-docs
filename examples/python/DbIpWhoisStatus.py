"""Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPWHOISApi(ApiClient(config))

result = api.db_ip_whois_status()
print(result)
