// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.ipReputation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);
