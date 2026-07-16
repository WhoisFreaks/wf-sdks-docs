"""Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_city(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCity.gz")
