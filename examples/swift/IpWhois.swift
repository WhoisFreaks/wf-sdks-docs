// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await IPWHOISAPI.ipWhois(apiKey: "YOUR_API_KEY", ip: "8.8.8.8", format: nil)
    print(result)
} catch {
    print(error)
}
