// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DomainReputationApi

fun main() {
    val api = DomainReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DomainReputation("YOUR_API_KEY", "example.com", null)
    println(result)  // status via api.DomainReputationWithHttpInfo(...).statusCode
}
