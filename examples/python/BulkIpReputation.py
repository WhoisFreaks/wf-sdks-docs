"""Runnable example: Bulk IP Reputation (POST /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi
from whoisfreaks.models.bulk_ip_reputation_request import BulkIpReputationRequest

# Parameters for bulkIpReputation (POST /v1.0/security):
#   - body: BulkIpReputationRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPReputationApi(ApiClient(config))

bulk_ip_reputation_request = BulkIpReputationRequest()  # populate fields as needed
result = api.bulk_ip_reputation(bulk_ip_reputation_request=bulk_ip_reputation_request)
print(result)
