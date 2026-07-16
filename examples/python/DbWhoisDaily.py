"""Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_daily(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisDaily.gz")
