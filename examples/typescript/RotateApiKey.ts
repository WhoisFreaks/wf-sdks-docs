// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.rotateApiKey({  });
  console.log(result);
}
main().catch(console.error);
