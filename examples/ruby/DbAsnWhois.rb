# Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - date (string, required)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesASNWHOISApi.new
result = api.db_asn_whois((Date.today - 1).to_s)
puts result
