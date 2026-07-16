// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = GeolocationApi()
    val result = api.bulkGeolocation(BulkGeolocationRequest())
    println(result)
}
