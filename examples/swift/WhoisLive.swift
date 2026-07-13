// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}
