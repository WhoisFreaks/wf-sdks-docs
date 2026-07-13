// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import Foundation
import WhoisFreaks

SubdomainsAPI.Subdomains(apiKey: "YOUR_API_KEY", domain: "example.com", after: "2000-01-01", before: String(ISO8601DateFormatter().string(from: Date()).prefix(10)), status: nil, page: nil, format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
