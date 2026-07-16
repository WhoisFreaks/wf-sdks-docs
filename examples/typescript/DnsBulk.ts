// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import { Configuration, DNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DNSApi(config);

async function main() {
  const result = await api.dnsBulk({ type: "value", dnsBulkRequest: {}, format: undefined });
  console.log(result);
}
main().catch(console.error);
