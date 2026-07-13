# Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::SSLApi.new
data, status, _headers = api.ssl_lookup_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data
