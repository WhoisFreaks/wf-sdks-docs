// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.bulkWhoisRaw({ apiKey: "YOUR_API_KEY", bulkWhoisRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
