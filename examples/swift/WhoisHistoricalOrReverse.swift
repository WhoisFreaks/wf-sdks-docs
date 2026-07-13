// Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
// Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (string (one of: historical, reverse), required)
//   - domainName (string, required): Required for historical lookup
//   - keyword (string, optional): For reverse — domain keyword search
//   - email (string, optional): For reverse — registrant email search
//   - owner (string, optional): For reverse — registrant name search
//   - company (string, optional): For reverse — company name search
//   - mode (string (one of: default, mini), optional)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

WHOISAPI.WhoisHistoricalOrReverse(apiKey: "YOUR_API_KEY", whois: "historical", domainName: "example.com", exact: true, keyword: nil, email: nil, owner: nil, company: nil, mode: nil, page: nil, format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
