// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPGeolocationApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPGeolocationApi } = require("whoisfreaks-js");)

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCityRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
