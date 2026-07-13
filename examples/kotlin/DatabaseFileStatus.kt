// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.databaseFileStatus()
    println(result)  // status via api.databaseFileStatusWithHttpInfo(...).statusCode
}
