// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DomainAvailabilityApi } = pkg;
// (CommonJS alternative: const { Configuration, DomainAvailabilityApi } = require("whoisfreaks-js");)

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.domainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
