// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

GeolocationAPI.Geolocation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
