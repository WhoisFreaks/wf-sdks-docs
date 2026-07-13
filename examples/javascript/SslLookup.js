// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, SSLApi } = pkg;
// (CommonJS alternative: const { Configuration, SSLApi } = require("whoisfreaks-js");)

const api = new SSLApi(new Configuration());

async function main() {
  const resp = await api.sslLookupRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
