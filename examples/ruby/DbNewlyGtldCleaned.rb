# Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_gtld_cleaned((Date.today - 1).to_s)
puts result
