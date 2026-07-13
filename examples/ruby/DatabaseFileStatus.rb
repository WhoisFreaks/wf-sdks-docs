# Runnable example: Database File Status (Public) (GET /v3.3/status)
# Parameters for databaseFileStatus (GET /v3.3/status):
#   (no parameters besides apiKey)
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.database_file_status_with_http_info()
puts "status: #{status}"
puts data
