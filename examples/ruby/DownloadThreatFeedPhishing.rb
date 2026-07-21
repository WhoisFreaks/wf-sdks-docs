# Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
# Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
#   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesThreatFeedApi.new
result = api.download_threat_feed_phishing((Date.today - 1).to_s)
puts result
