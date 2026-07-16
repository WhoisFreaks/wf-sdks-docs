// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbDroppedBacklinks(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
