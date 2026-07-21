// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = AccountApi()
    val result = api.databaseFileStatus()
    println(result)
}
