# Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesASNWHOISApi.new
data, status, _headers = api.db_asn_whois_with_http_info(api_key: "YOUR_API_KEY", date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
