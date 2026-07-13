// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

do {
    let result = try await IPReputationAPI.ipReputation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8")
    print(result)
} catch {
    print(error)
}
