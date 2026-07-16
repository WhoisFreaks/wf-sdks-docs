# Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DNSApi.new
result = api.dns_bulk("value", WhoisFreaks::DnsBulkRequest.new)
puts result
