// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkIpReputationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = IPReputationApi()
    val result = api.bulkIpReputation(BulkIpReputationRequest())
    println(result)
}
