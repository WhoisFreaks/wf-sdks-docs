// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DNSApi } = pkg;
// (CommonJS alternative: const { Configuration, DNSApi } = require("whoisfreaks-js");)

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsBulkRaw({ apiKey: "YOUR_API_KEY", type: "value", dnsBulkRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
