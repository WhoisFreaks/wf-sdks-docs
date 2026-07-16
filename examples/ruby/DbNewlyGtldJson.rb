# Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_gtld_json((Date.today - 1).to_s)
puts result
