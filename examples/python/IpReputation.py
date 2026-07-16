"""Runnable example: IP Reputation Lookup (GET /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi

# Parameters for ipReputation (GET /v1.0/security):
#   - ip (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPReputationApi(ApiClient(config))

result = api.ip_reputation(ip="8.8.8.8")
print(result)
