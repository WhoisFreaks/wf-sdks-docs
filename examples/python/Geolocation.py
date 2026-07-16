"""Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi

# Parameters for geolocation (GET /v1.0/geolocation):
#   - ip (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = GeolocationApi(ApiClient(config))

result = api.geolocation(ip="8.8.8.8")
print(result)
