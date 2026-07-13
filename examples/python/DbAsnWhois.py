"""Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

data = api.db_asn_whois(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbAsnWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbAsnWhois.gz")
