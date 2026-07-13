// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCountryStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
