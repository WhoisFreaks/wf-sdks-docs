// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.bulkIpReputation({ bulkIpReputationRequest: {} });
  console.log(result);
}
main().catch(console.error);
