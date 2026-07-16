// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesWHOISAPI.dbWhoisDaily(date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}
