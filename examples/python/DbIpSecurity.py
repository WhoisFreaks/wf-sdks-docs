"""Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPSecurityApi(ApiClient(config))

data = api.db_ip_security(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpSecurity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpSecurity.gz")
