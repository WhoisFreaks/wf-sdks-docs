// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, IPWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, IPWHOISApi } = require("whoisfreaks-js");)

const api = new IPWHOISApi(new Configuration());

async function main() {
  const resp = await api.ipWhoisRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
