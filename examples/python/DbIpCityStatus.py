"""Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

result = api.db_ip_city_status()
print(result)
