// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import WhoisFreaks

do {
    let result = try await DomainAvailabilityAPI.bulkDomainAvailabilityV2(apiKey: "YOUR_API_KEY", bulkDomainAvailabilityRequest: BulkDomainAvailabilityRequest(), domain: nil, format: nil)
    print(result)
} catch {
    print(error)
}
