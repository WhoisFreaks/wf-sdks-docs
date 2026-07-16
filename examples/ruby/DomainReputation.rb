# Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
# Parameters for domainReputation (GET /v1/domain/security):
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DomainReputationApi.new
result = api.domain_reputation("example.com")
puts result
