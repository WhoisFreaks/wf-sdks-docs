# Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
# Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesThreatFeedApi.new
result = api.download_threat_feed_spam_sample()
puts result
