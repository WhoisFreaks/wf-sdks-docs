// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesASNWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesASNWHOISApi } = require("whoisfreaks-js");)

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
