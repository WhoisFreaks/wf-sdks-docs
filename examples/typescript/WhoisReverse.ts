// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisReverse({ keyword: "value", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);
