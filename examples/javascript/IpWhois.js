// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, IPWHOISApi } = pkg;
// or:  const { ApiClient, IPWHOISApi } = require("whoisfreaks-js");

const api = new IPWHOISApi();   // uses ApiClient.instance

api.ipWhois("YOUR_API_KEY", "8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));
