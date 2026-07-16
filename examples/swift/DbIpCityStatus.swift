// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCityStatus()
    print(result)
} catch {
    print(error)
}
