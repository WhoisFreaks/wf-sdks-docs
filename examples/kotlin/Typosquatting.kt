// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.api.TyposquattingApi

fun main() {
    val api = TyposquattingApi(basePath = "https://api.whoisfreaks.com")
    val result = api.typosquatting("YOUR_API_KEY", null, null, null)
    println(result)  // status via api.typosquattingWithHttpInfo(...).statusCode
}
