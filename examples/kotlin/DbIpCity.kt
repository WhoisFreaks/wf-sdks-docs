// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCity("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpCityWithHttpInfo(...).statusCode
}
