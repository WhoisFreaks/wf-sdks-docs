# Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.rotate_api_key_with_http_info(api_key: "YOUR_API_KEY")
puts "status: #{status}"
puts data
