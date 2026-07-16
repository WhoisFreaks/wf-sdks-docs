"""Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.rotate_api_key()
print(result)
