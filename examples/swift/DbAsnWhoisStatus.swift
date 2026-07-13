// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesASNWHOISAPI.dbAsnWhoisStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
