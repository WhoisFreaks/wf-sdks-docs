# Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DomainAvailabilityApi.new
result = api.domain_availability_v2("example.com")
puts result
