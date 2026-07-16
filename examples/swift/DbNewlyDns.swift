// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesNewlyRegisteredAPI.dbNewlyDns(date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}
