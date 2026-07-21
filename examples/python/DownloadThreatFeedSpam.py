"""Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
#   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_spam(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("downloadThreatFeedSpam.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedSpam.gz")
