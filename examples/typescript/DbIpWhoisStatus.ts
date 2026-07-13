// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const api = new DatabasesIPWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbIpWhoisStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
