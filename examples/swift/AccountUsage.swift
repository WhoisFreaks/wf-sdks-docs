// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await AccountAPI.accountUsage(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
