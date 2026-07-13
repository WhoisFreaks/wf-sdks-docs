// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.api.IPReputationApi
import com.whoisfreaks.models.BulkGeolocationRequest

fun main() {
    val api = IPReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.BulkIpReputation("YOUR_API_KEY", BulkGeolocationRequest())
    println(result)  // status via api.BulkIpReputationWithHttpInfo(...).statusCode
}
