// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import WhoisFreaks

WHOISAPI.BulkWhois(apiKey: "YOUR_API_KEY", bulkWhoisRequest: BulkWhoisRequest(), format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
