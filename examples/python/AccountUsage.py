"""Runnable example: Account Usage (GET /v1.0/whoisapi/usage)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.account_usage()
print(result)
