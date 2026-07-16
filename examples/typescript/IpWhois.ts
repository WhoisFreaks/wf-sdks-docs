// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, IPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPWHOISApi(config);

async function main() {
  const result = await api.ipWhois({ ip: "8.8.8.8", format: undefined });
  console.log(result);
}
main().catch(console.error);
