// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, AccountApi } = pkg;
// or:  const { ApiClient, AccountApi } = require("whoisfreaks-js");

const api = new AccountApi();   // uses ApiClient.instance

api.rotateApiKey("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));
