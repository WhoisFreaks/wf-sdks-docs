// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.accountUsage({  });
  console.log(result);
}
main().catch(console.error);
