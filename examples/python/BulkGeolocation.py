"""Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = GeolocationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
result = api.bulk_geolocation(bulk_geolocation_request=bulk_geolocation_request)
print(result)
