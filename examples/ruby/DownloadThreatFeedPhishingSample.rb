# Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
# Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesThreatFeedApi.new
result = api.download_threat_feed_phishing_sample()
puts result
