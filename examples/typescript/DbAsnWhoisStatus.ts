// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesASNWHOISApi(config);

async function main() {
  const result = await api.dbAsnWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);
