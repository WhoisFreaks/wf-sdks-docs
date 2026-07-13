// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const api = new TyposquattingApi(new Configuration());

async function main() {
  const resp = await api.typosquattingRaw({ apiKey: "YOUR_API_KEY", keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
