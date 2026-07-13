// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import WhoisFreaks

TyposquattingAPI.Typosquatting(apiKey: "YOUR_API_KEY", keyword: nil, pattern: nil, pageToken: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
