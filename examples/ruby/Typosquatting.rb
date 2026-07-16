# Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::TyposquattingApi.new
result = api.typosquatting()
puts result
