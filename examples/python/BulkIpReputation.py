"""Runnable example: Bulk IP Reputation (POST /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkIpReputation (POST /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
api = IPReputationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
resp = api.bulk_ip_reputation_with_http_info(api_key="YOUR_API_KEY", bulk_geolocation_request=bulk_geolocation_request)
print("status:", resp.status_code)
print(resp.data)
