// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesNewlyRegisteredApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");)

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyCctldRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
