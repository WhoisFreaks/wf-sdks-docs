// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import WhoisFreaks

IPReputationAPI.BulkIpReputation(apiKey: "YOUR_API_KEY", bulkGeolocationRequest: BulkGeolocationRequest()) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
