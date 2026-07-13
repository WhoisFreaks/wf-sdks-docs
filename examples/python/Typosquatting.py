"""Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.typosquatting_api import TyposquattingApi

# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
config = Configuration()
api = TyposquattingApi(ApiClient(config))

resp = api.typosquatting_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
