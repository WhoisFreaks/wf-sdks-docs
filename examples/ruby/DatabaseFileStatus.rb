# Runnable example: Database File Status (Public) (GET /v3.4/status)
# Parameters for databaseFileStatus (GET /v3.4/status):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::AccountApi.new
result = api.database_file_status()
puts result
