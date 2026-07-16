"""Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld_cleaned(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtldCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtldCleaned.gz")
