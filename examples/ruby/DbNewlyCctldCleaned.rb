# Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
# Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_cctld_cleaned((Date.today - 1).to_s)
puts result
