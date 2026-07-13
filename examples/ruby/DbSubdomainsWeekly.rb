# Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesSubdomainsApi.new
data, status, _headers = api.db_subdomains_weekly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
