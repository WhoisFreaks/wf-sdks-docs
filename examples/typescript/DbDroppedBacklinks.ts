// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbDroppedBacklinksRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
