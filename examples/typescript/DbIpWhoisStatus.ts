// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPWHOISApi(config);

async function main() {
  const result = await api.dbIpWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);
