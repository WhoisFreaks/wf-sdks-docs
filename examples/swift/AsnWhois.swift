// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await ASNWHOISAPI.asnWhois(apiKey: "YOUR_API_KEY", asn: "AS15169", format: nil)
    print(result)
} catch {
    print(error)
}
