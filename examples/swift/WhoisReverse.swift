// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisReverse(apiKey: "YOUR_API_KEY", keyword: "value", page: nil, format: nil)
    print(result)
} catch {
    print(error)
}
