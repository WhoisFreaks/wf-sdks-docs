// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbDroppedJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);
