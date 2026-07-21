"""Runnable example: Database File Status (Public) (GET /v3.4/status)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for databaseFileStatus (GET /v3.4/status):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.database_file_status()
print(result)
