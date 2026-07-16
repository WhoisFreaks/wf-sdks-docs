# Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_gtld(false, (Date.today - 1).to_s)
puts result
