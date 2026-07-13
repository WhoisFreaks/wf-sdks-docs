// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

do {
    let result = try await GeolocationAPI.geolocation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8")
    print(result)
} catch {
    print(error)
}
