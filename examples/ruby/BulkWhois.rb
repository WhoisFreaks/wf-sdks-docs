# Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.bulk_whois_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkWhoisRequest.new)
puts "status: #{status}"
puts data
