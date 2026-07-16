"""Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPSecurityApi(ApiClient(config))

result = api.db_ip_security_status()
print(result)
