# Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::SSLApi.new
result = api.ssl_lookup("example.com")
puts result
