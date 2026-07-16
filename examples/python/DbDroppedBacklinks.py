"""Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_dropped_backlinks(whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDroppedBacklinks.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDroppedBacklinks.gz")
