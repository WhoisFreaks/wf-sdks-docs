# Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
# Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_cctld(false, (Date.today - 1).to_s)
puts result
