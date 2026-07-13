// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import Foundation
import WhoisFreaks

DatabasesExpiringDroppedAPI.DbDroppedJson(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)), tlds: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
