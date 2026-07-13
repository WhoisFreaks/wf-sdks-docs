"""Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ssl_api import SSLApi

# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = SSLApi(ApiClient(config))

resp = api.ssl_lookup_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)
