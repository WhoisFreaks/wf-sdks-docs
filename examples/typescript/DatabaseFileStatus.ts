// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.databaseFileStatus({  });
  console.log(result);
}
main().catch(console.error);
