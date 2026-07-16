# TypeScript SDK

## About

The official **WhoisFreaks TypeScript SDK** — a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from TypeScript with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to npm.

**Keywords:** typescript whois api, typescript whois sdk, whoisfreaks typescript, typescript domain lookup, typescript dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** npm
- **Package:** `whoisfreaks`

## Install

```bash
npm install whoisfreaks
```

## Build from Source

Prefer to build the SDK yourself instead of installing from npm? Clone the monorepo and build the TypeScript package locally:

```bash
git clone https://github.com/WhoisFreaks/wf-sdks
cd wf-sdks/sdks/typescript
npm install
npm run build
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

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

const result = await api.whoisLive({ domainName: "example.com" });
console.log(result);
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
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisLive({ domainName: "example.com", format: undefined });
  console.log(result);
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
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisLive({ domainName: "example.com", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```typescript
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.bulkWhois({ bulkWhoisRequest: {}, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```typescript
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisHistory({ domainName: "example.com", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```typescript
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisReverse({ keyword: "value", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```typescript
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

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```typescript
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DNSApi(config);

async function main() {
  const result = await api.dnsHistorical({ domainName: "example.com", type: "value", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```typescript
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DNSApi(config);

async function main() {
  const result = await api.dnsReverse({ value: "value", type: "a", exact: true, page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```typescript
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import { Configuration, DNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DNSApi(config);

async function main() {
  const result = await api.dnsBulk({ type: "value", dnsBulkRequest: {}, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```typescript
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainAvailabilityApi(config);

async function main() {
  const result = await api.domainAvailabilityV2({ domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```typescript
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainAvailabilityApi(config);

async function main() {
  const result = await api.bulkDomainAvailabilityV2({ bulkDomainAvailabilityRequest: {}, domain: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```typescript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new TyposquattingApi(config);

async function main() {
  const result = await api.typosquatting({ keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log(result);
}
main().catch(console.error);

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```typescript
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SSLApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SSLApi(config);

async function main() {
  const result = await api.sslLookup({ domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```typescript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.geolocation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```typescript
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.bulkGeolocation({ bulkGeolocationRequest: {} });
  console.log(result);
}
main().catch(console.error);

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```typescript
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SubdomainsApi(config);

async function main() {
  const result = await api.subdomains({ domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```typescript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.ipReputation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);

```

#### Bulk IP Reputation

`POST /v1.0/security`

```typescript
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.bulkIpReputation({ bulkIpReputationRequest: {} });
  console.log(result);
}
main().catch(console.error);

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```typescript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainReputationApi(config);

async function main() {
  const result = await api.domainReputation({ domainName: "example.com", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```typescript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, ASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new ASNWHOISApi(config);

async function main() {
  const result = await api.asnWhois({ asn: "AS15169", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```typescript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, IPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPWHOISApi(config);

async function main() {
  const result = await api.ipWhois({ ip: "8.8.8.8", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```typescript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.rotateApiKey({  });
  console.log(result);
}
main().catch(console.error);

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```typescript
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.accountUsage({  });
  console.log(result);
}
main().catch(console.error);

```

#### Database File Status (Public)

`GET /v3.3/status`

```typescript
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.databaseFileStatus({  });
  console.log(result);
}
main().catch(console.error);

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```typescript
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtld({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```typescript
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctld({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```typescript
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtldCleaned({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```typescript
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctldCleaned({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```typescript
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtldJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```typescript
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctldJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```typescript
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyDns({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```typescript
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbExpired({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```typescript
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbExpiredCleaned({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```typescript
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbDropped({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```typescript
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbDroppedJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```typescript
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesExpiringDroppedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesExpiringDroppedApi(config);

async function main() {
  const result = await api.dbDroppedBacklinks({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```typescript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisDaily({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```typescript
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisWeekly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```typescript
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisMonthly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```typescript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesDNSApi(config);

async function main() {
  const result = await api.dbDnsDaily({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```typescript
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesDNSApi(config);

async function main() {
  const result = await api.dbDnsWeekly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```typescript
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesDNSApi(config);

async function main() {
  const result = await api.dbDnsMonthly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```typescript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesSubdomainsApi(config);

async function main() {
  const result = await api.dbSubdomainsDaily({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```typescript
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesSubdomainsApi(config);

async function main() {
  const result = await api.dbSubdomainsWeekly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```typescript
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesSubdomainsApi(config);

async function main() {
  const result = await api.dbSubdomainsMonthly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```typescript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCountryStatus({  });
  console.log(result);
}
main().catch(console.error);

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```typescript
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCountry({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```typescript
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCityStatus({  });
  console.log(result);
}
main().catch(console.error);

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```typescript
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCity({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```typescript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesASNWHOISApi(config);

async function main() {
  const result = await api.dbAsnWhois({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```typescript
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesASNWHOISApi(config);

async function main() {
  const result = await api.dbAsnWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```typescript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPWHOISApi(config);

async function main() {
  const result = await api.dbIpWhois({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```typescript
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPWHOISApi(config);

async function main() {
  const result = await api.dbIpWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```typescript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPSecurityApi(config);

async function main() {
  const result = await api.dbIpSecurity({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```typescript
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPSecurityApi(config);

async function main() {
  const result = await api.dbIpSecurityStatus({  });
  console.log(result);
}
main().catch(console.error);

```
