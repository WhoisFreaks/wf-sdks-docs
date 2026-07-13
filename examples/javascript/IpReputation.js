// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, IPReputationApi } = pkg;
// (CommonJS alternative: const { Configuration, IPReputationApi } = require("whoisfreaks-js");)

const api = new IPReputationApi(new Configuration());

async function main() {
  const resp = await api.ipReputationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
