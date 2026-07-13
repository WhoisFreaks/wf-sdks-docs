# Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DomainAvailabilityApi.new
data, status, _headers = api.domain_availability_v2_with_http_info(api_key: "YOUR_API_KEY", domain: "example.com")
puts "status: #{status}"
puts data
