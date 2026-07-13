"""Runnable example: Domain Reputation Lookup (GET /v1/domain/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_reputation_api import DomainReputationApi

# Parameters for domainReputation (GET /v1/domain/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainReputationApi(ApiClient(config))

resp = api.domain_reputation_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)
