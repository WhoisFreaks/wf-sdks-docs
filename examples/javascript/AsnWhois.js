// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, ASNWHOISApi } = pkg;
// or:  const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new ASNWHOISApi(client);

api.asnWhois("AS15169")
  .then(data => console.log(data))
  .catch(err => console.error(err));
