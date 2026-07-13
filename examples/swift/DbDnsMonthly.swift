// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

DatabasesDNSAPI.DbDnsMonthly(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10))) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
