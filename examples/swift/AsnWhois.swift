// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

ASNWHOISAPI.AsnWhois(apiKey: "YOUR_API_KEY", asn: "AS15169", format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
