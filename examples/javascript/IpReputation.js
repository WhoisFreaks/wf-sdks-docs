// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, IPReputationApi } = pkg;
// or:  const { ApiClient, IPReputationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new IPReputationApi(client);

api.ipReputation("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));
