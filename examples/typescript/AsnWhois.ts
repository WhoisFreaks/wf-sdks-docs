// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, ASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new ASNWHOISApi(config);

async function main() {
  const result = await api.asnWhois({ asn: "AS15169", format: undefined });
  console.log(result);
}
main().catch(console.error);
