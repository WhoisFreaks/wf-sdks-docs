// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkDomainAvailabilityRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DomainAvailabilityApi()
    val result = api.bulkDomainAvailabilityV2(BulkDomainAvailabilityRequest(), null, null)
    println(result)
}
