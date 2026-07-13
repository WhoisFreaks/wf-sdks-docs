// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, IPReputationApi } = pkg;
// (CommonJS alternative: const { Configuration, IPReputationApi } = require("whoisfreaks-js");)

const api = new IPReputationApi(new Configuration());

async function main() {
  const resp = await api.bulkIpReputationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
