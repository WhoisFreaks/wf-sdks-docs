// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

DatabasesASNWHOISAPI.DbAsnWhoisStatus(apiKey: "YOUR_API_KEY") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
