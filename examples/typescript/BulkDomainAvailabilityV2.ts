// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainAvailabilityApi(config);

async function main() {
  const result = await api.bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest: {}, domain: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);
