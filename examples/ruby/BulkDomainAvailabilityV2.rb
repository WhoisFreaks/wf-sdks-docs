# Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DomainAvailabilityApi.new
result = api.bulk_domain_availability_v2(WhoisFreaks::BulkDomainAvailabilityRequest.new)
puts result
