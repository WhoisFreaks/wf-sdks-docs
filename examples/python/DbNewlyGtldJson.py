"""Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

resp = api.db_newly_gtld_json_with_http_info(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))
print("status:", resp.status_code)
print(resp.data)
