// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, IPWHOISApi } = pkg;
// or:  const { ApiClient, IPWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new IPWHOISApi(client);

api.ipWhois("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));
