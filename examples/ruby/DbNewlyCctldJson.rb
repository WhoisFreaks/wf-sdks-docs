# Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_cctld_json((Date.today - 1).to_s)
puts result
