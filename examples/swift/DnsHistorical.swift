// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DNSAPI.dnsHistorical(apiKey: "YOUR_API_KEY", domainName: "example.com", type: "value", page: nil, format: nil)
    print(result)
} catch {
    print(error)
}
