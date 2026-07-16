"""Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesASNWHOISApi(ApiClient(config))

result = api.db_asn_whois_status()
print(result)
