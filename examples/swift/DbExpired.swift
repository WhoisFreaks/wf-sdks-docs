// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

DatabasesExpiringDroppedAPI.DbExpired(apiKey: "YOUR_API_KEY", whois: false, date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10))) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
