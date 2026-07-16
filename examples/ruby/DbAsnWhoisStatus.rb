# Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesASNWHOISApi.new
result = api.db_asn_whois_status()
puts result
