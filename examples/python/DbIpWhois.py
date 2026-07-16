"""Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPWHOISApi(ApiClient(config))

data = api.db_ip_whois(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpWhois.gz")
