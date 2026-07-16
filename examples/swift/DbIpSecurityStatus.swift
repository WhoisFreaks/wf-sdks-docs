// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import WhoisFreaks

// Set your API key once (applied to every request)
WhoisFreaksAPI.apiKey = "YOUR_API_KEY"

do {
    let result = try await DatabasesIPSecurityAPI.dbIpSecurityStatus()
    print(result)
} catch {
    print(error)
}
