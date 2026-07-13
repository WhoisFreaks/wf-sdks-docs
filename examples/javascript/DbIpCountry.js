// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const api = new DatabasesIPGeolocationApi();   // uses ApiClient.instance

api.dbIpCountry("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
