// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const api = new DatabasesNewlyRegisteredApi();   // uses ApiClient.instance

api.dbNewlyCctldJson("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
