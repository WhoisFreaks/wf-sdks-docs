"""Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_monthly(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisMonthly.gz")
