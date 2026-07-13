"""Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsWeekly.gz")
