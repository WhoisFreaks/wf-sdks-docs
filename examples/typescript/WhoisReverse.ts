// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisReverseRaw({ apiKey: "YOUR_API_KEY", keyword: "value", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
