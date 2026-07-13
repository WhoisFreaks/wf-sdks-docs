"""Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest

# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
config = Configuration()
api = DNSApi(ApiClient(config))

dns_bulk_request = DnsBulkRequest()  # populate fields as needed
resp = api.dns_bulk_with_http_info(api_key="YOUR_API_KEY", var_type="value", dns_bulk_request=dns_bulk_request)
print("status:", resp.status_code)
print(resp.data)
