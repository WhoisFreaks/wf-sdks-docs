// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.api.DomainAvailabilityApi
import com.whoisfreaks.models.BulkDomainAvailabilityRequest

fun main() {
    val api = DomainAvailabilityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkDomainAvailabilityV2("YOUR_API_KEY", BulkDomainAvailabilityRequest(), null, null)
    println(result)  // status via api.bulkDomainAvailabilityV2WithHttpInfo(...).statusCode
}
