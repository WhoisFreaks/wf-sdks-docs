// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesDNSApi } = pkg;
// or:  const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesDNSApi(client);

api.dbDnsWeekly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));
