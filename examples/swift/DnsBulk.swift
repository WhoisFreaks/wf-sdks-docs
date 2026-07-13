// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import WhoisFreaks

do {
    let result = try await DNSAPI.dnsBulk(apiKey: "YOUR_API_KEY", type: "value", dnsBulkRequest: DnsBulkRequest(), format: nil)
    print(result)
} catch {
    print(error)
}
