// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPSecurityApi(config);

async function main() {
  const result = await api.dbIpSecurityStatus({  });
  console.log(result);
}
main().catch(console.error);
