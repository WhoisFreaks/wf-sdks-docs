# Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_cctld_json_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
