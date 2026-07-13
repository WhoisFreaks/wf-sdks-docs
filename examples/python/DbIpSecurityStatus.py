"""Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPSecurityApi(ApiClient(config))

resp = api.db_ip_security_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
