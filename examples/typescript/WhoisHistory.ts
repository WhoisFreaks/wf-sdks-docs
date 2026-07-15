// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisHistoryRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
