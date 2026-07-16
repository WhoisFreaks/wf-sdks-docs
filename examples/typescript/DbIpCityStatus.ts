// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCityStatus({  });
  console.log(result);
}
main().catch(console.error);
