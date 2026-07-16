# Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::AccountApi.new
result = api.rotate_api_key()
puts result
