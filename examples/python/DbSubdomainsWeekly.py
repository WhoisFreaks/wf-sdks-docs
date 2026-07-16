"""Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_weekly(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsWeekly.gz")
