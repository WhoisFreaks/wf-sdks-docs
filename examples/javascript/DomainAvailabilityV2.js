// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DomainAvailabilityApi } = pkg;
// or:  const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

const api = new DomainAvailabilityApi();   // uses ApiClient.instance

api.domainAvailabilityV2("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));
