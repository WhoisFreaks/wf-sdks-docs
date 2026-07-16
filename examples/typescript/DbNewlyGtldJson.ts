// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtldJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);
