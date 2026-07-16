"""Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ssl_api import SSLApi

# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = SSLApi(ApiClient(config))

result = api.ssl_lookup(domain_name="example.com")
print(result)
