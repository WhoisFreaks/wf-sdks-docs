// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SubdomainsApi(config);

async function main() {
  const result = await api.subdomains({ domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);
