# Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesASNWHOISApi.new
data, status, _headers = api.db_asn_whois_status_with_http_info(api_key: "YOUR_API_KEY")
puts "status: #{status}"
puts data
