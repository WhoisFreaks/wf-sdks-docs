// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesThreatFeedApi } = pkg;
// or:  const { ApiClient, DatabasesThreatFeedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesThreatFeedApi(client);

api.downloadThreatFeedSpamSample()
  .then(data => console.log(data))
  .catch(err => console.error(err));
