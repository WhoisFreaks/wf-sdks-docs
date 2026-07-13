// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesWHOISApi

fun main() {
    val api = DatabasesWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbWhoisMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbWhoisMonthlyWithHttpInfo(...).statusCode
}
