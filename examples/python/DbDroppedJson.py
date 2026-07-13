"""Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

resp = api.db_dropped_json_with_http_info(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))
print("status:", resp.status_code)
print(resp.data)
