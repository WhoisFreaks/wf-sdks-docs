// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import Foundation
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesNewlyRegisteredAPI.dbNewlyGtld(whois: false, date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)), tlds: nil)
    print(result)
} catch {
    print(error)
}
