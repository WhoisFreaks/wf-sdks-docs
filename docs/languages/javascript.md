# JavaScript SDK

## About

The official **WhoisFreaks JavaScript SDK** — a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from JavaScript with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to npm.

**Keywords:** javascript whois api, javascript whois sdk, whoisfreaks javascript, javascript domain lookup, javascript dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** npm
- **Package:** `whoisfreaks-js`

## Install

```bash
npm install whoisfreaks-js
```

## Build from Source

Prefer to build the SDK yourself instead of installing from npm? Clone the monorepo and build the JavaScript package locally:

```bash
git clone https://github.com/WhoisFreaks/wf-sdks
cd wf-sdks/sdks/javascript
npm install
npm run build
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
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.whoisLive("example.com")
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
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.whoisLive("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

## Endpoints

All 54 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```javascript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.whoisLive("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```javascript
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.bulkWhois({})
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```javascript
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.whoisHistory("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```javascript
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new WHOISApi(client);

api.whoisReverse("value")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```javascript
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DNSApi(client);

api.dnsLive("example.com", "8.8.8.8", "value")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```javascript
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DNSApi(client);

api.dnsHistorical("example.com", "value")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```javascript
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DNSApi(client);

api.dnsReverse("value", "a", true)
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```javascript
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DNSApi } = pkg;
// or:  const { ApiClient, DNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DNSApi(client);

api.dnsBulk("value", {})
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```javascript
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DomainAvailabilityApi } = pkg;
// or:  const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DomainAvailabilityApi(client);

api.domainAvailabilityV2("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```javascript
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DomainAvailabilityApi } = pkg;
// or:  const { ApiClient, DomainAvailabilityApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DomainAvailabilityApi(client);

api.bulkDomainAvailabilityV2({})
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```javascript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, TyposquattingApi } = pkg;
// or:  const { ApiClient, TyposquattingApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new TyposquattingApi(client);

api.typosquatting()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```javascript
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, SSLApi } = pkg;
// or:  const { ApiClient, SSLApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new SSLApi(client);

api.sslLookup("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```javascript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, GeolocationApi } = pkg;
// or:  const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new GeolocationApi(client);

api.geolocation("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```javascript
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, GeolocationApi } = pkg;
// or:  const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new GeolocationApi(client);

api.bulkGeolocation({})
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```javascript
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, SubdomainsApi } = pkg;
// or:  const { ApiClient, SubdomainsApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new SubdomainsApi(client);

api.subdomains("example.com", "2000-01-01", new Date().toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```javascript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, IPReputationApi } = pkg;
// or:  const { ApiClient, IPReputationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new IPReputationApi(client);

api.ipReputation("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Bulk IP Reputation

`POST /v1.0/security`

```javascript
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, IPReputationApi } = pkg;
// or:  const { ApiClient, IPReputationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new IPReputationApi(client);

api.bulkIpReputation({})
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```javascript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DomainReputationApi } = pkg;
// or:  const { ApiClient, DomainReputationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DomainReputationApi(client);

api.domainReputation("example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```javascript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, ASNWHOISApi } = pkg;
// or:  const { ApiClient, ASNWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new ASNWHOISApi(client);

api.asnWhois("AS15169")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```javascript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, IPWHOISApi } = pkg;
// or:  const { ApiClient, IPWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new IPWHOISApi(client);

api.ipWhois("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```javascript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, AccountApi } = pkg;
// or:  const { ApiClient, AccountApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new AccountApi(client);

api.rotateApiKey()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```javascript
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, AccountApi } = pkg;
// or:  const { ApiClient, AccountApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new AccountApi(client);

api.accountUsage()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Database File Status (Public)

`GET /v3.3/status`

```javascript
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, AccountApi } = pkg;
// or:  const { ApiClient, AccountApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new AccountApi(client);

api.databaseFileStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```javascript
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyGtld(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```javascript
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyCctld(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```javascript
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyGtldCleaned(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```javascript
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyCctldCleaned(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```javascript
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyGtldJson(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```javascript
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyCctldJson(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```javascript
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesNewlyRegisteredApi } = pkg;
// or:  const { ApiClient, DatabasesNewlyRegisteredApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesNewlyRegisteredApi(client);

api.dbNewlyDns(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```javascript
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbExpired(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```javascript
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbExpiredCleaned(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```javascript
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbDropped(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```javascript
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbDroppedJson(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```javascript
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesExpiringDroppedApi } = pkg;
// or:  const { ApiClient, DatabasesExpiringDroppedApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesExpiringDroppedApi(client);

api.dbDroppedBacklinks(false, new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```javascript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesWHOISApi(client);

api.dbWhoisDaily(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```javascript
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesWHOISApi(client);

api.dbWhoisWeekly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```javascript
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesWHOISApi(client);

api.dbWhoisMonthly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```javascript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesDNSApi } = pkg;
// or:  const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesDNSApi(client);

api.dbDnsDaily(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```javascript
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesDNSApi } = pkg;
// or:  const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesDNSApi(client);

api.dbDnsWeekly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```javascript
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesDNSApi } = pkg;
// or:  const { ApiClient, DatabasesDNSApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesDNSApi(client);

api.dbDnsMonthly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```javascript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesSubdomainsApi } = pkg;
// or:  const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesSubdomainsApi(client);

api.dbSubdomainsDaily(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```javascript
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesSubdomainsApi } = pkg;
// or:  const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesSubdomainsApi(client);

api.dbSubdomainsWeekly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```javascript
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesSubdomainsApi } = pkg;
// or:  const { ApiClient, DatabasesSubdomainsApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesSubdomainsApi(client);

api.dbSubdomainsMonthly(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```javascript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPGeolocationApi(client);

api.dbIpCountryStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```javascript
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPGeolocationApi(client);

api.dbIpCountry(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```javascript
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPGeolocationApi(client);

api.dbIpCityStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```javascript
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPGeolocationApi } = pkg;
// or:  const { ApiClient, DatabasesIPGeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPGeolocationApi(client);

api.dbIpCity(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```javascript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesASNWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesASNWHOISApi(client);

api.dbAsnWhois(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```javascript
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesASNWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesASNWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesASNWHOISApi(client);

api.dbAsnWhoisStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```javascript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPWHOISApi(client);

api.dbIpWhois(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```javascript
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPWHOISApi } = pkg;
// or:  const { ApiClient, DatabasesIPWHOISApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPWHOISApi(client);

api.dbIpWhoisStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```javascript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPSecurityApi } = pkg;
// or:  const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPSecurityApi(client);

api.dbIpSecurity(new Date(Date.now()-86400000).toISOString().slice(0,10))
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```javascript
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, DatabasesIPSecurityApi } = pkg;
// or:  const { ApiClient, DatabasesIPSecurityApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new DatabasesIPSecurityApi(client);

api.dbIpSecurityStatus()
  .then(data => console.log(data))
  .catch(err => console.error(err));

```
