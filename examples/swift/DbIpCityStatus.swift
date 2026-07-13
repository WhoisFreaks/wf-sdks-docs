// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

DatabasesIPGeolocationAPI.DbIpCityStatus(apiKey: "YOUR_API_KEY") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
