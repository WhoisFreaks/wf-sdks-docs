# Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_gtld_with_http_info(api_key: "YOUR_API_KEY", whois: false, date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
