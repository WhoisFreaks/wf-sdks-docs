// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new TyposquattingApi(config);

async function main() {
  const result = await api.typosquatting({ keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log(result);
}
main().catch(console.error);
