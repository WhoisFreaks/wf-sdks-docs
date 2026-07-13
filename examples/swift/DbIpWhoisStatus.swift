// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesIPWHOISAPI.dbIpWhoisStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}
