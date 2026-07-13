// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await AccountAPI.rotateApiKey(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
