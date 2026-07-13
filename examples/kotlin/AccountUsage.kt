// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.AccountUsage("YOUR_API_KEY")
    println(result)  // status via api.AccountUsageWithHttpInfo(...).statusCode
}
