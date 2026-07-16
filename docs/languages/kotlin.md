# Kotlin SDK

## About

The official **WhoisFreaks Kotlin SDK** — a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Kotlin with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Maven Central.

**Keywords:** kotlin whois api, kotlin whois sdk, whoisfreaks kotlin, kotlin domain lookup, kotlin dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** Maven Central
- **Package:** `com.whoisfreaks:whoisfreaks`

## Install

```kotlin
implementation("com.whoisfreaks:whoisfreaks:LATEST")
```

## Build from Source

Prefer to build the SDK yourself instead of installing from Maven Central? Clone the monorepo and build the Kotlin package locally:

```bash
git clone https://github.com/WhoisFreaks/wf-sdks
cd wf-sdks/sdks/kotlin
./gradlew build   # or: ./gradlew publishToMavenLocal
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

In a Gradle project, add to `build.gradle.kts`:

```kotlin
repositories { mavenCentral() }
dependencies {
    implementation("com.whoisfreaks:whoisfreaks:LATEST")   // pin to a real version, e.g. 1.0.0
}
```

`src/main/kotlin/Main.kt`:

```kotlin
import com.whoisfreaks.client.apis.WhoisApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WhoisApi()
    val result = api.whoisLive("example.com")
    println(result)
}
```

Run with `./gradlew run` (with the application plugin) or your IDE.

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.whoisLive("example.com", null)
    println(result)
}

```

## Endpoints

All 54 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.whoisLive("example.com", null)
    println(result)
}

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```kotlin
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkWhoisRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.bulkWhois(BulkWhoisRequest(), null)
    println(result)
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```kotlin
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.whoisHistory("example.com", null, null)
    println(result)
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```kotlin
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.whoisReverse("value", null, null)
    println(result)
}

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```kotlin
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsLive("example.com", "8.8.8.8", "value", null)
    println(result)
}

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```kotlin
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsHistorical("example.com", "value", null, null)
    println(result)
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```kotlin
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsReverse("value", "a", true, null, null)
    println(result)
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```kotlin
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.DnsBulkRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsBulk("value", DnsBulkRequest(), null)
    println(result)
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```kotlin
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DomainAvailabilityApi()
    val result = api.domainAvailabilityV2("example.com", null, null, null)
    println(result)
}

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```kotlin
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.client.apis.DomainAvailabilityApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkDomainAvailabilityRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DomainAvailabilityApi()
    val result = api.bulkDomainAvailabilityV2(BulkDomainAvailabilityRequest(), null, null)
    println(result)
}

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```kotlin
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.client.apis.TyposquattingApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = TyposquattingApi()
    val result = api.typosquatting(null, null, null)
    println(result)
}

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```kotlin
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.SSLApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = SSLApi()
    val result = api.sslLookup("example.com", null, null, null)
    println(result)
}

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```kotlin
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = GeolocationApi()
    val result = api.geolocation("8.8.8.8")
    println(result)
}

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```kotlin
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.apis.GeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkGeolocationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = GeolocationApi()
    val result = api.bulkGeolocation(BulkGeolocationRequest())
    println(result)
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```kotlin
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.SubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = SubdomainsApi()
    val result = api.subdomains("example.com", "2000-01-01", java.time.LocalDate.now().toString(), null, null, null)
    println(result)
}

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```kotlin
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = IPReputationApi()
    val result = api.ipReputation("8.8.8.8")
    println(result)
}

```

#### Bulk IP Reputation

`POST /v1.0/security`

```kotlin
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import com.whoisfreaks.client.apis.IPReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkIpReputationRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = IPReputationApi()
    val result = api.bulkIpReputation(BulkIpReputationRequest())
    println(result)
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```kotlin
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DomainReputationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DomainReputationApi()
    val result = api.domainReputation("example.com", null)
    println(result)
}

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```kotlin
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.ASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = ASNWHOISApi()
    val result = api.asnWhois("AS15169", null)
    println(result)
}

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```kotlin
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.IPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = IPWHOISApi()
    val result = api.ipWhois("8.8.8.8", null)
    println(result)
}

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```kotlin
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = AccountApi()
    val result = api.rotateApiKey()
    println(result)
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```kotlin
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = AccountApi()
    val result = api.accountUsage()
    println(result)
}

```

#### Database File Status (Public)

`GET /v3.3/status`

```kotlin
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.AccountApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = AccountApi()
    val result = api.databaseFileStatus()
    println(result)
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyGtld(false, java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyCctld(false, java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```kotlin
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyGtldCleaned(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```kotlin
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyCctldCleaned(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyGtldJson(java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyCctldJson(java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```kotlin
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyDns(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```kotlin
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbExpired(false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```kotlin
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbExpiredCleaned(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```kotlin
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbDropped(false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```kotlin
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbDroppedJson(java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```kotlin
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbDroppedBacklinks(false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```kotlin
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesWHOISApi()
    val result = api.dbWhoisDaily(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesWHOISApi()
    val result = api.dbWhoisWeekly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesWHOISApi()
    val result = api.dbWhoisMonthly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```kotlin
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesDNSApi()
    val result = api.dbDnsDaily(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```kotlin
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesDNSApi()
    val result = api.dbDnsWeekly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```kotlin
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesDNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesDNSApi()
    val result = api.dbDnsMonthly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```kotlin
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesSubdomainsApi()
    val result = api.dbSubdomainsDaily(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```kotlin
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesSubdomainsApi()
    val result = api.dbSubdomainsWeekly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```kotlin
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesSubdomainsApi()
    val result = api.dbSubdomainsMonthly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPGeolocationApi()
    val result = api.dbIpCountryStatus()
    println(result)
}

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPGeolocationApi()
    val result = api.dbIpCountry(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPGeolocationApi()
    val result = api.dbIpCityStatus()
    println(result)
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPGeolocationApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPGeolocationApi()
    val result = api.dbIpCity(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesASNWHOISApi()
    val result = api.dbAsnWhois(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesASNWHOISApi()
    val result = api.dbAsnWhoisStatus()
    println(result)
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPWHOISApi()
    val result = api.dbIpWhois(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPWHOISApi()
    val result = api.dbIpWhoisStatus()
    println(result)
}

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPSecurityApi()
    val result = api.dbIpSecurity(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPSecurityApi()
    val result = api.dbIpSecurityStatus()
    println(result)
}

```
