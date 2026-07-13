// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DomainAvailabilityApi } = pkg;
// (CommonJS alternative: const { Configuration, DomainAvailabilityApi } = require("whoisfreaks-js");)

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.bulkDomainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", bulkDomainAvailabilityRequest: {}, domain: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
