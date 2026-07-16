// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCountryStatus({  });
  console.log(result);
}
main().catch(console.error);
