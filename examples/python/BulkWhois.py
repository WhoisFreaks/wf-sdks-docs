"""Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest

# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

bulk_whois_request = BulkWhoisRequest()  # populate fields as needed
result = api.bulk_whois(bulk_whois_request=bulk_whois_request)
print(result)
