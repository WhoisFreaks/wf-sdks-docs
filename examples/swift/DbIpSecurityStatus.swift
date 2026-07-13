// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesIPSecurityAPI.dbIpSecurityStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
