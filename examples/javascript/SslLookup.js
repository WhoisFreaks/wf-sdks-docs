// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, SSLApi } = pkg;
// or:  const { ApiClient, SSLApi } = require("whoisfreaks-js");

const api = new SSLApi();   // uses ApiClient.instance

api.sslLookup("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));
