// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesExpiringDroppedApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");)

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbExpiredCleanedRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
