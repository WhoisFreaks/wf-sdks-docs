// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await SSLAPI.sslLookup(apiKey: "YOUR_API_KEY", domainName: "example.com", chain: nil, sslRaw: nil, format: nil)
    print(result)
} catch {
    print(error)
}
