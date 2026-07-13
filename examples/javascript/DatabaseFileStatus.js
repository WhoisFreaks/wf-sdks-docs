// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, AccountApi } = pkg;
// (CommonJS alternative: const { Configuration, AccountApi } = require("whoisfreaks-js");)

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.databaseFileStatusRaw({  });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
