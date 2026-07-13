// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesDNSApi

fun main() {
    val api = DatabasesDNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbDnsDaily("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.DbDnsDailyWithHttpInfo(...).statusCode
}
