"""Runnable example: Database File Status (Public) (GET /v3.3/status)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for databaseFileStatus (GET /v3.3/status):
#   (no parameters besides apiKey)
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.database_file_status_with_http_info()
print("status:", resp.status_code)
print(resp.data)
