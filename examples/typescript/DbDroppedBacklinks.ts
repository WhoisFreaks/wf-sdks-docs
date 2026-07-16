// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbDroppedBacklinks({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);
