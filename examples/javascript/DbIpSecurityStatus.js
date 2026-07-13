// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPSecurityApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPSecurityApi } = require("whoisfreaks-js");)

const api = new DatabasesIPSecurityApi(new Configuration());

async function main() {
  const resp = await api.dbIpSecurityStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
