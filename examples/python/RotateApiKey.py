"""Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.rotate_api_key_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
