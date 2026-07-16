// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesSubdomainsApi(config);

async function main() {
  const result = await api.dbSubdomainsMonthly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);
