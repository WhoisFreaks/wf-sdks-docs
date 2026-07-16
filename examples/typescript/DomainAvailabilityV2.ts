// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainAvailabilityApi(config);

async function main() {
  const result = await api.domainAvailabilityV2({ domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);
