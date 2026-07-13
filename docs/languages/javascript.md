# JavaScript SDK

- **Registry:** npm
- **Package:** `whoisfreaks-js`

## Install

```bash
npm install whoisfreaks-js
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
npm init -y
npm install whoisfreaks-js
```

Create `main.js`:

```js
// whoisfreaks-js is CommonJS: import the default, then destructure
import pkg from "whoisfreaks-js";
const { Configuration, WHOISApi } = pkg;
// or:  const { Configuration, WHOISApi } = require("whoisfreaks-js");

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
```

Run it:

```bash
node main.js
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```javascript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, WHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, WHOISApi } = require("whoisfreaks-js");)

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

## Endpoints

All 53 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

`GET /v2.0/whois/live`

```javascript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, WHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, WHOISApi } = require("whoisfreaks-js");)

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### DNS: Live DNS Lookup

`GET /v2.0/dns/live`

```javascript
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

```

### Domain Availability: Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```javascript
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DomainAvailabilityApi } = pkg;
// (CommonJS alternative: const { Configuration, DomainAvailabilityApi } = require("whoisfreaks-js");)

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.domainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Typosquatting: Typosquatting Lookup

`GET /v3.0/domain/typos`

```javascript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, TyposquattingApi } = pkg;
// (CommonJS alternative: const { Configuration, TyposquattingApi } = require("whoisfreaks-js");)

const api = new TyposquattingApi(new Configuration());

async function main() {
  const resp = await api.typosquattingRaw({ apiKey: "YOUR_API_KEY", keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### SSL: SSL Certificate Lookup

`GET /v1.0/ssl/live`

```javascript
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, SSLApi } = pkg;
// (CommonJS alternative: const { Configuration, SSLApi } = require("whoisfreaks-js");)

const api = new SSLApi(new Configuration());

async function main() {
  const resp = await api.sslLookupRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```javascript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, GeolocationApi } = pkg;
// (CommonJS alternative: const { Configuration, GeolocationApi } = require("whoisfreaks-js");)

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.geolocationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Subdomains: Subdomains Lookup

`GET /v1.0/subdomains`

```javascript
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, SubdomainsApi } = pkg;
// (CommonJS alternative: const { Configuration, SubdomainsApi } = require("whoisfreaks-js");)

const api = new SubdomainsApi(new Configuration());

async function main() {
  const resp = await api.subdomainsRaw({ apiKey: "YOUR_API_KEY", domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```javascript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, IPReputationApi } = pkg;
// (CommonJS alternative: const { Configuration, IPReputationApi } = require("whoisfreaks-js");)

const api = new IPReputationApi(new Configuration());

async function main() {
  const resp = await api.ipReputationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```javascript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DomainReputationApi } = pkg;
// (CommonJS alternative: const { Configuration, DomainReputationApi } = require("whoisfreaks-js");)

const api = new DomainReputationApi(new Configuration());

async function main() {
  const resp = await api.domainReputationRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```javascript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, ASNWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, ASNWHOISApi } = require("whoisfreaks-js");)

const api = new ASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.asnWhoisRaw({ apiKey: "YOUR_API_KEY", asn: "AS15169", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```javascript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, IPWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, IPWHOISApi } = require("whoisfreaks-js");)

const api = new IPWHOISApi(new Configuration());

async function main() {
  const resp = await api.ipWhoisRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```javascript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, AccountApi } = pkg;
// (CommonJS alternative: const { Configuration, AccountApi } = require("whoisfreaks-js");)

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.rotateApiKeyRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Newly Registered: Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```javascript
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesNewlyRegisteredApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");)

const api = new DatabasesNewlyRegisteredApi(new Configuration());

async function main() {
  const resp = await api.dbNewlyGtldRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```javascript
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesExpiringDroppedApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");)

const api = new DatabasesExpiringDroppedApi(new Configuration());

async function main() {
  const resp = await api.dbExpiredRaw({ apiKey: "YOUR_API_KEY", whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```javascript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesWHOISApi } = require("whoisfreaks-js");)

const api = new DatabasesWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbWhoisDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```javascript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesDNSApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesDNSApi } = require("whoisfreaks-js");)

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```javascript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesSubdomainsApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesSubdomainsApi } = require("whoisfreaks-js");)

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```javascript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPGeolocationApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPGeolocationApi } = require("whoisfreaks-js");)

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCountryStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```javascript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesASNWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesASNWHOISApi } = require("whoisfreaks-js");)

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```javascript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPWHOISApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPWHOISApi } = require("whoisfreaks-js");)

const api = new DatabasesIPWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbIpWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```javascript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, DatabasesIPSecurityApi } = pkg;
// (CommonJS alternative: const { Configuration, DatabasesIPSecurityApi } = require("whoisfreaks-js");)

const api = new DatabasesIPSecurityApi(new Configuration());

async function main() {
  const resp = await api.dbIpSecurityRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```
