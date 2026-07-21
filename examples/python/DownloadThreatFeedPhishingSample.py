"""Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_phishing_sample()   # bytes
with open("downloadThreatFeedPhishingSample.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedPhishingSample.gz")
