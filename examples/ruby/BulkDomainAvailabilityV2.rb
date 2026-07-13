# Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::DomainAvailabilityApi.new
data, status, _headers = api.bulk_domain_availability_v2_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkDomainAvailabilityRequest.new)
puts "status: #{status}"
puts data
