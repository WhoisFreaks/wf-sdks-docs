// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedPhishing({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);
