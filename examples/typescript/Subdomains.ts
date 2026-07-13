// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SubdomainsApi } from "whoisfreaks";

const api = new SubdomainsApi(new Configuration());

async function main() {
  const resp = await api.subdomainsRaw({ apiKey: "YOUR_API_KEY", domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
