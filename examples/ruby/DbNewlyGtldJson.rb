# Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_gtld_json_with_http_info(api_key: "YOUR_API_KEY", date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
