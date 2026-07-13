// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

AccountAPI.RotateApiKey(apiKey: "YOUR_API_KEY") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
