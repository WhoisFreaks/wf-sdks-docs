// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesNewlyRegisteredAPI.dbNewlyCctld(apiKey: "YOUR_API_KEY", whois: false, date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)), tlds: nil)
    print(result)
} catch {
    print(error)
}
