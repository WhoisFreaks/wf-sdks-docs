# Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::AccountApi.new
result = api.account_usage()
puts result
