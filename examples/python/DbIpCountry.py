"""Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_country(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCountry.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCountry.gz")
