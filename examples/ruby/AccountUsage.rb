# Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.account_usage_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
