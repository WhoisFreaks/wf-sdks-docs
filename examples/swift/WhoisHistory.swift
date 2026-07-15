// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisHistory(apiKey: "YOUR_API_KEY", domainName: "example.com", page: nil, format: nil)
    print(result)
} catch {
    print(error)
}
