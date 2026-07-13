// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DNSApi } = pkg;
// (CommonJS alternative: const { Configuration, DNSApi } = require("whoisfreaks-js");)

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsHistoricalRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", type: "value", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
