// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPWHOISApi } = require("whoisfreaks-js");)

const api = new DatabasesIPWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbIpWhoisStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
