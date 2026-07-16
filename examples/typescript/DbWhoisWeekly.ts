// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisWeekly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);
