// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

SSLAPI.SslLookup(apiKey: "YOUR_API_KEY", domainName: "example.com", chain: nil, sslRaw: nil, format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
