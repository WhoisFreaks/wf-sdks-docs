// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import WhoisFreaks

do {
    let result = try await TyposquattingAPI.typosquatting(apiKey: "YOUR_API_KEY", keyword: nil, pattern: nil, pageToken: nil)
    print(result)
} catch {
    print(error)
}
