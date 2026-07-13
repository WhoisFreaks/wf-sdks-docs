// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

DatabasesNewlyRegisteredAPI.DbNewlyCctldCleaned(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10))) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
