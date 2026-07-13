# Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
# Parameters for domainReputation (GET /v1/domain/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DomainReputationApi.new
data, status, _headers = api.domain_reputation_with_http_info(api_key: "YOUR_API_KEY", domain_name: "example.com")
puts "status: #{status}"
puts data
