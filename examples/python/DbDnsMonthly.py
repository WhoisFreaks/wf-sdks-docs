"""Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_monthly(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsMonthly.gz")
