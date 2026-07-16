# TypeScript SDK

- **Registry:** npm
- **Package:** `whoisfreaks`

## Install

```bash
npm install whoisfreaks
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
npm init -y
npm install whoisfreaks
npm install -D typescript ts-node @types/node
```

Set `"type": "module"` in `package.json`, then create `main.ts`:

```ts
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com" });
console.log("status:", resp.raw.status);
console.log(await resp.value());
```

Run it:

```bash
npx ts-node main.ts
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```typescript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

## Endpoints

All 54 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```typescript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```typescript
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.bulkWhoisRaw({ apiKey: "YOUR_API_KEY", bulkWhoisRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```typescript
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisHistoryRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```typescript
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisReverseRaw({ apiKey: "YOUR_API_KEY", keyword: "value", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```typescript
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```typescript
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsHistoricalRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", type: "value", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```typescript
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsReverseRaw({ apiKey: "YOUR_API_KEY", value: "value", type: "a", exact: true, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```typescript
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsBulkRaw({ apiKey: "YOUR_API_KEY", type: "value", dnsBulkRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```typescript
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.domainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```typescript
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.bulkDomainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", bulkDomainAvailabilityRequest: {}, domain: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```typescript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const api = new TyposquattingApi(new Configuration());

async function main() {
  const resp = await api.typosquattingRaw({ apiKey: "YOUR_API_KEY", keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```typescript
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SSLApi } from "whoisfreaks";

const api = new SSLApi(new Configuration());

async function main() {
  const resp = await api.sslLookupRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```typescript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import { Configuration, GeolocationApi } from "whoisfreaks";

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.geolocationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```typescript
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.bulkGeolocationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```typescript
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SubdomainsApi } from "whoisfreaks";

const api = new SubdomainsApi(new Configuration());

async function main() {
  const resp = await api.subdomainsRaw({ apiKey: "YOUR_API_KEY", domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```typescript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import { Configuration, IPReputationApi } from "whoisfreaks";

const api = new IPReputationApi(new Configuration());

async function main() {
  const resp = await api.ipReputationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Bulk IP Reputation

`POST /v1.0/security`

```typescript
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, IPReputationApi } from "whoisfreaks";

const api = new IPReputationApi(new Configuration());

async function main() {
  const resp = await api.bulkIpReputationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```typescript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainReputationApi } from "whoisfreaks";

const api = new DomainReputationApi(new Configuration());

async function main() {
  const resp = await api.domainReputationRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```typescript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, ASNWHOISApi } from "whoisfreaks";

const api = new ASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.asnWhoisRaw({ apiKey: "YOUR_API_KEY", asn: "AS15169", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```typescript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, IPWHOISApi } from "whoisfreaks";

const api = new IPWHOISApi(new Configuration());

async function main() {
  const resp = await api.ipWhoisRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```typescript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.rotateApiKeyRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```typescript
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.accountUsageRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Database File Status (Public)

`GET /v3.3/status`

```typescript
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.databaseFileStatusRaw({  });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```typescript
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyGtldRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```typescript
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyCctldRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```typescript
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyGtldCleanedRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```typescript
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyCctldCleanedRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```typescript
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyGtldJsonRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```typescript
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyCctldJsonRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```typescript
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyDnsRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```typescript
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbExpiredRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```typescript
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbExpiredCleanedRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```typescript
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbDroppedRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```typescript
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbDroppedJsonRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```typescript
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbDroppedBacklinksRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```typescript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const api = new DatabasesWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbWhoisDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```typescript
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const api = new DatabasesWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbWhoisWeeklyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```typescript
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const api = new DatabasesWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbWhoisMonthlyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```typescript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```typescript
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsWeeklyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```typescript
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsMonthlyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```typescript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```typescript
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsWeeklyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```typescript
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsMonthlyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```typescript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCountryStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```typescript
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCountryRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```typescript
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCityStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```typescript
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCityRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```typescript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```typescript
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```typescript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const api = new DatabasesIPWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbIpWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```typescript
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const api = new DatabasesIPWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbIpWhoisStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```typescript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const api = new DatabasesIPSecurityApi(new Configuration());

async function main() {
  const resp = await api.dbIpSecurityRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```typescript
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const api = new DatabasesIPSecurityApi(new Configuration());

async function main() {
  const resp = await api.dbIpSecurityStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```
