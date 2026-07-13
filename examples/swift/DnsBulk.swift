// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import WhoisFreaks

DNSAPI.DnsBulk(apiKey: "YOUR_API_KEY", type: "value", dnsBulkRequest: DnsBulkRequest(), format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
