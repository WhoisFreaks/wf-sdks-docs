// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

IPReputationAPI.IpReputation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8") { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
