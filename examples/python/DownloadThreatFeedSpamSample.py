"""Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_spam_sample()   # bytes
with open("downloadThreatFeedSpamSample.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedSpamSample.gz")
