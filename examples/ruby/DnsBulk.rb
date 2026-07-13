# Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_bulk_with_http_info("YOUR_API_KEY", "value", WhoisFreaks::DnsBulkRequest.new)
puts "status: #{status}"
puts data
