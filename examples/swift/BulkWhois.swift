// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import WhoisFreaks

do {
    let result = try await WHOISAPI.bulkWhois(apiKey: "YOUR_API_KEY", bulkWhoisRequest: BulkWhoisRequest(), format: nil)
    print(result)
} catch {
    print(error)
}
