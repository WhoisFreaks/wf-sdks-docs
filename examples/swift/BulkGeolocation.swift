// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import WhoisFreaks

GeolocationAPI.BulkGeolocation(apiKey: "YOUR_API_KEY", bulkGeolocationRequest: BulkGeolocationRequest()) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
