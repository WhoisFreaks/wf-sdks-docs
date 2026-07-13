// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

DomainAvailabilityAPI.DomainAvailabilityV2(apiKey: "YOUR_API_KEY", domain: "example.com", sug: nil, count: nil, format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
