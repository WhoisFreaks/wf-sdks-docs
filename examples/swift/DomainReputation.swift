// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DomainReputationAPI.domainReputation(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}
