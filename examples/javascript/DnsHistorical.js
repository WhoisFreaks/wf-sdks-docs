// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const api = new DNSApi();   // uses ApiClient.instance

api.dnsHistorical("YOUR_API_KEY", "example.com", "value")
  .then(data => console.log(data))
  .catch(err => console.error(err));
