"""Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

resp = api.db_asn_whois_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)
