# Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::WHOISApi.new
result = api.bulk_whois(WhoisFreaks::BulkWhoisRequest.new)
puts result
