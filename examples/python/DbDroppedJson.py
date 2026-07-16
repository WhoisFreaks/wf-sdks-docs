"""Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesExpiringDroppedApi(ApiClient(config))

result = api.db_dropped_json(var_date=str(date.today() - timedelta(days=1)))
print(result)
