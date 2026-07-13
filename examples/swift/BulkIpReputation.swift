// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import WhoisFreaks

do {
    let result = try await IPReputationAPI.bulkIpReputation(apiKey: "YOUR_API_KEY", bulkGeolocationRequest: BulkGeolocationRequest())
    print(result)
} catch {
    print(error)
}
