// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await IPReputationAPI.bulkIpReputation(bulkIpReputationRequest: BulkIpReputationRequest())
    print(result)
} catch {
    print(error)
}
