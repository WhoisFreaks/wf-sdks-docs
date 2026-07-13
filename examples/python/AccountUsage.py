"""Runnable example: Account Usage (GET /v1.0/whoisapi/usage)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.account_usage_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
