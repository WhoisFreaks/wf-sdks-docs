"""Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi

# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainAvailabilityApi(ApiClient(config))

resp = api.domain_availability_v2_with_http_info(api_key="YOUR_API_KEY", domain="example.com")
print("status:", resp.status_code)
print(resp.data)
