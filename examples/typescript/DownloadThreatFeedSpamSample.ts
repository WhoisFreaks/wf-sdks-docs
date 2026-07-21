// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedSpamSample({  });
  console.log(result);
}
main().catch(console.error);
