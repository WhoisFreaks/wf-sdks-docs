// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.RotateApiKey("YOUR_API_KEY")
    println(result)  // status via api.RotateApiKeyWithHttpInfo(...).statusCode
}
