"""Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi

# Parameters for geolocation (GET /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
config = Configuration()
api = GeolocationApi(ApiClient(config))

resp = api.geolocation_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)
