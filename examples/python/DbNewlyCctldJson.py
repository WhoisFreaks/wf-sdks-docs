"""Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

result = api.db_newly_cctld_json(var_date=str(date.today() - timedelta(days=1)))
print(result)
