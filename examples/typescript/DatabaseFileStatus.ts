// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.databaseFileStatusRaw({  });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
