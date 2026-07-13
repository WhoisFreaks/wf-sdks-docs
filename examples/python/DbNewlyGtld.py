"""Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtld.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtld.gz")
