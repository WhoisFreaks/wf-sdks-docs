// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.api.GeolocationApi

fun main() {
    val api = GeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.geolocation("YOUR_API_KEY", "8.8.8.8")
    println(result)  // status via api.geolocationWithHttpInfo(...).statusCode
}
