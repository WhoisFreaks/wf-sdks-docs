"""Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.typosquatting_api import TyposquattingApi

# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = TyposquattingApi(ApiClient(config))

result = api.typosquatting()
print(result)
