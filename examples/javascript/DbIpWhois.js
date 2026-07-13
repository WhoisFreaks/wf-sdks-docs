// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

const api = new DatabasesIPWHOISApi();   // uses ApiClient.instance

api.dbIpWhois("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
