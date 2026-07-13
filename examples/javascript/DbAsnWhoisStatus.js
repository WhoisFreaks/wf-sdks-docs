// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesASNWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

const api = new DatabasesASNWHOISApi();   // uses ApiClient.instance

api.dbAsnWhoisStatus("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));
