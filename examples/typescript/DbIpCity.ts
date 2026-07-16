// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCity({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);
