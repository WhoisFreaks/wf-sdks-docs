// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbIpCityStatus("YOUR_API_KEY")
    println(result)  // status via api.DbIpCityStatusWithHttpInfo(...).statusCode
}
