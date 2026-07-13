"""Runnable example: IP Reputation Lookup (GET /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi

# Parameters for ipReputation (GET /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
config = Configuration()
api = IPReputationApi(ApiClient(config))

resp = api.ip_reputation_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)
