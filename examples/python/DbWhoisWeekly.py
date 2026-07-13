"""Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisWeekly.gz")
