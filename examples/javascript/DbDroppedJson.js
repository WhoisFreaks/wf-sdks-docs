// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesExpiringDroppedApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");)

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbDroppedJsonRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
