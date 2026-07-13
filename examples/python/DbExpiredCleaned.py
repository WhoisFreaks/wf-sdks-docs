"""Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_expired_cleaned(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbExpiredCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbExpiredCleaned.gz")
