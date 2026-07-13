// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DNSAPI.dnsReverse(apiKey: "YOUR_API_KEY", value: "value", type: "a", exact: true, page: nil, format: nil)
    print(result)
} catch {
    print(error)
}
