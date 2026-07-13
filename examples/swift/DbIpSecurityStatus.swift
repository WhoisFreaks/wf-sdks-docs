// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

DatabasesIPSecurityAPI.DbIpSecurityStatus(apiKey: "YOUR_API_KEY") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
