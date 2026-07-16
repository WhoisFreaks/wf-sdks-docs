// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SSLApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SSLApi(config);

async function main() {
  const result = await api.sslLookup({ domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);
