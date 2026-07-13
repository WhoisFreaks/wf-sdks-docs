# Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
# Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (string (one of: historical, reverse), required)
#   - domainName (string, required): Required for historical lookup
#   - keyword (string, optional): For reverse — domain keyword search
#   - email (string, optional): For reverse — registrant email search
#   - owner (string, optional): For reverse — registrant name search
#   - company (string, optional): For reverse — company name search
#   - mode (string (one of: default, mini), optional)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_historical_or_reverse_with_http_info(api_key: "YOUR_API_KEY", whois: "historical", domain_name: "example.com", exact: true)
puts "status: #{status}"
puts data
