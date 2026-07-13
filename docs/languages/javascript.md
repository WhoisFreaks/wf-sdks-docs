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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const api = new WHOISApi();   // uses ApiClient.instance

api.whoisLive("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));
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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const api = new WHOISApi();   // uses ApiClient.instance

api.whoisLive("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const api = new WHOISApi();   // uses ApiClient.instance

api.whoisLive("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const api = new DNSApi();   // uses ApiClient.instance

api.dnsLive("YOUR_API_KEY", "example.com", "8.8.8.8", "value")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DomainAvailabilityApi } = pkg;
// or:  const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

const api = new DomainAvailabilityApi();   // uses ApiClient.instance

api.domainAvailabilityV2("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, TyposquattingApi } = pkg;
// or:  const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

const api = new TyposquattingApi();   // uses ApiClient.instance

api.typosquatting("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, SSLApi } = pkg;
// or:  const { ApiClient, SSLApi } = require("whoisfreaks-js");

const api = new SSLApi();   // uses ApiClient.instance

api.sslLookup("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```javascript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, GeolocationApi } = pkg;
// or:  const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

const api = new GeolocationApi();   // uses ApiClient.instance

api.geolocation("YOUR_API_KEY", "8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, SubdomainsApi } = pkg;
// or:  const { ApiClient, SubdomainsApi } = require("whoisfreaks-js");

const api = new SubdomainsApi();   // uses ApiClient.instance

api.subdomains("YOUR_API_KEY", "example.com", "2000-01-01", new Date().toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```javascript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, IPReputationApi } = pkg;
// or:  const { ApiClient, IPReputationApi } = require("whoisfreaks-js");

const api = new IPReputationApi();   // uses ApiClient.instance

api.ipReputation("YOUR_API_KEY", "8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```javascript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DomainReputationApi } = pkg;
// or:  const { ApiClient, DomainReputationApi } = require("whoisfreaks-js");

const api = new DomainReputationApi();   // uses ApiClient.instance

api.domainReputation("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```javascript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, ASNWHOISApi } = pkg;
// or:  const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

const api = new ASNWHOISApi();   // uses ApiClient.instance

api.asnWhois("YOUR_API_KEY", "AS15169")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```javascript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, IPWHOISApi } = pkg;
// or:  const { ApiClient, IPWHOISApi } = require("whoisfreaks-js");

const api = new IPWHOISApi();   // uses ApiClient.instance

api.ipWhois("YOUR_API_KEY", "8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```javascript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, AccountApi } = pkg;
// or:  const { ApiClient, AccountApi } = require("whoisfreaks-js");

const api = new AccountApi();   // uses ApiClient.instance

api.rotateApiKey("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));

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
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const api = new DatabasesNewlyRegisteredApi();   // uses ApiClient.instance

api.dbNewlyGtld("YOUR_API_KEY", false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```javascript
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const api = new DatabasesExpiringDroppedApi();   // uses ApiClient.instance

api.dbExpired("YOUR_API_KEY", false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```javascript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

const api = new DatabasesWHOISApi();   // uses ApiClient.instance

api.dbWhoisDaily("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```javascript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesDNSApi } = pkg;
// or:  const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

const api = new DatabasesDNSApi();   // uses ApiClient.instance

api.dbDnsDaily("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```javascript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesSubdomainsApi } = pkg;
// or:  const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

const api = new DatabasesSubdomainsApi();   // uses ApiClient.instance

api.dbSubdomainsDaily("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```javascript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const api = new DatabasesIPGeolocationApi();   // uses ApiClient.instance

api.dbIpCountryStatus("YOUR_API_KEY")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```javascript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesASNWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

const api = new DatabasesASNWHOISApi();   // uses ApiClient.instance

api.dbAsnWhois("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```javascript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

const api = new DatabasesIPWHOISApi();   // uses ApiClient.instance

api.dbIpWhois("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```javascript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPSecurityApi } = pkg;
// or:  const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

const api = new DatabasesIPSecurityApi();   // uses ApiClient.instance

api.dbIpSecurity("YOUR_API_KEY", new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```
