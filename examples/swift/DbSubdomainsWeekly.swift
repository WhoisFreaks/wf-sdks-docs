// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesSubdomainsAPI.dbSubdomainsWeekly(date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}
