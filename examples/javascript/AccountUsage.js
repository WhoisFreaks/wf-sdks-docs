// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, AccountApi } = pkg;
// (CommonJS alternative: const { Configuration, AccountApi } = require("whoisfreaks-js");)

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.accountUsageRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
