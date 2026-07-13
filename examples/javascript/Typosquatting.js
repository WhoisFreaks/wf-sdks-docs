// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, TyposquattingApi } = pkg;
// or:  const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

const api = new TyposquattingApi();   // uses ApiClient.instance

api.typosquatting("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));
