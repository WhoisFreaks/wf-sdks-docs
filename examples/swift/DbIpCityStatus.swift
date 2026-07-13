// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCityStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
