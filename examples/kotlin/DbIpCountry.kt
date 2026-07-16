// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPGeolocationApi()
    val result = api.dbIpCountry(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
