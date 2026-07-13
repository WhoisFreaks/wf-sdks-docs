"""Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

resp = api.db_ip_country_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
