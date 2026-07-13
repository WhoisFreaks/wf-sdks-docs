// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DomainReputationApi } = pkg;
// or:  const { ApiClient, DomainReputationApi } = require("whoisfreaks-js");

const api = new DomainReputationApi();   // uses ApiClient.instance

api.domainReputation("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));
