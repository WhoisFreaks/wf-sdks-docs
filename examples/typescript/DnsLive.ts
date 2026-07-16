// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DNSApi(config);

async function main() {
  const result = await api.dnsLive({ domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: undefined });
  console.log(result);
}
main().catch(console.error);
