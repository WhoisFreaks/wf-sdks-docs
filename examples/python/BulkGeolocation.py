"""Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
api = GeolocationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
resp = api.bulk_geolocation_with_http_info(api_key="YOUR_API_KEY", bulk_geolocation_request=bulk_geolocation_request)
print("status:", resp.status_code)
print(resp.data)
