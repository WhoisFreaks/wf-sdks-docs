// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

DatabasesIPGeolocationAPI.DbIpCountryStatus(apiKey: "YOUR_API_KEY") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
