// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

WHOISAPI.WhoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
