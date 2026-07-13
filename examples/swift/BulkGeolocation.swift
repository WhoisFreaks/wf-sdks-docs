// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import WhoisFreaks

do {
    let result = try await GeolocationAPI.bulkGeolocation(apiKey: "YOUR_API_KEY", bulkGeolocationRequest: BulkGeolocationRequest())
    print(result)
} catch {
    print(error)
}
