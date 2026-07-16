// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainReputationApi(config);

async function main() {
  const result = await api.domainReputation({ domainName: "example.com", format: undefined });
  console.log(result);
}
main().catch(console.error);
