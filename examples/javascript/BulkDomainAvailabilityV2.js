// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DomainAvailabilityApi } = pkg;
// or:  const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

const api = new DomainAvailabilityApi();   // uses ApiClient.instance

api.bulkDomainAvailabilityV2("YOUR_API_KEY", {})
  .then(data => console.log(data))
  .catch(err => console.error(err));
