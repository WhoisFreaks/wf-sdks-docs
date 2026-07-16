// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await TyposquattingAPI.typosquatting(keyword: nil, pattern: nil, pageToken: nil)
    print(result)
} catch {
    print(error)
}
