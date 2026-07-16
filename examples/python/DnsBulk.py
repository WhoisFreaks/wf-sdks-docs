"""Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest

# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DNSApi(ApiClient(config))

dns_bulk_request = DnsBulkRequest()  # populate fields as needed
result = api.dns_bulk(var_type="value", dns_bulk_request=dns_bulk_request)
print(result)
