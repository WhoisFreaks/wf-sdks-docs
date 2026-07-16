"""Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

result = api.db_ip_country_status()
print(result)
