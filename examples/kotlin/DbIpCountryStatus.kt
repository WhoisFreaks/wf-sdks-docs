// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCountryStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpCountryStatusWithHttpInfo(...).statusCode
}
