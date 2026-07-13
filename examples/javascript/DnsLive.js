// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DNSApi } = pkg;
// (CommonJS alternative: const { Configuration, DNSApi } = require("whoisfreaks-js");)

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
