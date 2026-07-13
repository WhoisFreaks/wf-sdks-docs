// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.api.GeolocationApi
import com.whoisfreaks.models.BulkGeolocationRequest

fun main() {
    val api = GeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkGeolocation("YOUR_API_KEY", BulkGeolocationRequest())
    println(result)  // status via api.bulkGeolocationWithHttpInfo(...).statusCode
}
