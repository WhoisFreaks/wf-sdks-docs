"""Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_expired(whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbExpired.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbExpired.gz")
