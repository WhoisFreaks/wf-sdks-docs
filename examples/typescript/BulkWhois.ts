// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.bulkWhois({ bulkWhoisRequest: {}, format: undefined });
  console.log(result);
}
main().catch(console.error);
