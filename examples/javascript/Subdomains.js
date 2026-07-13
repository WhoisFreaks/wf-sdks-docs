// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, SubdomainsApi } = pkg;
// or:  const { ApiClient, SubdomainsApi } = require("whoisfreaks-js");

const api = new SubdomainsApi();   // uses ApiClient.instance

api.subdomains("YOUR_API_KEY", "example.com", "2000-01-01", new Date().toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
