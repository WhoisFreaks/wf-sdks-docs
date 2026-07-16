// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DomainReputationApi } = pkg;
// or:  const { ApiClient, DomainReputationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DomainReputationApi(client);

api.domainReputation("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));
