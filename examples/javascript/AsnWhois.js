// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, ASNWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, ASNWHOISApi } = require("whoisfreaks-js");)

const api = new ASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.asnWhoisRaw({ apiKey: "YOUR_API_KEY", asn: "AS15169", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
