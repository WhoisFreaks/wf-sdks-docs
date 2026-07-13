// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const api = new DatabasesNewlyRegisteredApi();   // uses ApiClient.instance

api.dbNewlyGtld("YOUR_API_KEY", false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
