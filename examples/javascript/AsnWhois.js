// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, ASNWHOISApi } = pkg;
// or:  const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

const api = new ASNWHOISApi();   // uses ApiClient.instance

api.asnWhois("YOUR_API_KEY", "AS15169")
  .then(data => console.log(data))
  .catch(err => console.error(err));
