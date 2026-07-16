"""Runnable example: Domain Reputation Lookup (GET /v1/domain/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_reputation_api import DomainReputationApi

# Parameters for domainReputation (GET /v1/domain/security):
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DomainReputationApi(ApiClient(config))

result = api.domain_reputation(domain_name="example.com")
print(result)
