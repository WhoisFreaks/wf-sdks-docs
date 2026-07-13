# Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
require 'whoisfreaks'

api = WhoisFreaks::TyposquattingApi.new
data, status, _headers = api.typosquatting_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
