// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesDNSApi

fun main() {
    val api = DatabasesDNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDnsMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDnsMonthlyWithHttpInfo(...).statusCode
}
