// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbNewlyCctld("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.DbNewlyCctldWithHttpInfo(...).statusCode
}
