// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import Foundation
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesThreatFeedAPI.downloadThreatFeedPhishing(date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}
