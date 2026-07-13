// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

DomainReputationAPI.DomainReputation(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
