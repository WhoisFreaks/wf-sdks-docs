"""Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi
from whoisfreaks.models.bulk_domain_availability_request import BulkDomainAvailabilityRequest

# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DomainAvailabilityApi(ApiClient(config))

bulk_domain_availability_request = BulkDomainAvailabilityRequest()  # populate fields as needed
result = api.bulk_domain_availability_v2(bulk_domain_availability_request=bulk_domain_availability_request)
print(result)
