# Kotlin SDK

- **Registry:** Maven Central
- **Package:** `com.whoisfreaks:whoisfreaks`

## Install

```kotlin
implementation("com.whoisfreaks:whoisfreaks:LATEST")
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
import com.whoisfreaks.api.WhoisApi

fun main() {
    val api = WhoisApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisLive("YOUR_API_KEY", "example.com", null)
    println(result)
}
```

Run with `./gradlew run` (with the application plugin) or your IDE.

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisLive("YOUR_API_KEY", "example.com", null)
    println(result)  // status via api.whoisLiveWithHttpInfo(...).statusCode
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
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisLive("YOUR_API_KEY", "example.com", null)
    println(result)  // status via api.whoisLiveWithHttpInfo(...).statusCode
}

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```kotlin
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.api.WHOISApi
import com.whoisfreaks.models.BulkWhoisRequest

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkWhois("YOUR_API_KEY", BulkWhoisRequest(), null)
    println(result)  // status via api.bulkWhoisWithHttpInfo(...).statusCode
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```kotlin
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisHistory("YOUR_API_KEY", "example.com", null, null)
    println(result)  // status via api.whoisHistoryWithHttpInfo(...).statusCode
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```kotlin
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisReverse("YOUR_API_KEY", "value", null, null)
    println(result)  // status via api.whoisReverseWithHttpInfo(...).statusCode
}

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```kotlin
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DNSApi

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsLive("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null)
    println(result)  // status via api.dnsLiveWithHttpInfo(...).statusCode
}

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```kotlin
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DNSApi

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsHistorical("YOUR_API_KEY", "example.com", "value", null, null)
    println(result)  // status via api.dnsHistoricalWithHttpInfo(...).statusCode
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```kotlin
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DNSApi

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsReverse("YOUR_API_KEY", "value", "a", true, null, null)
    println(result)  // status via api.dnsReverseWithHttpInfo(...).statusCode
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```kotlin
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.api.DNSApi
import com.whoisfreaks.models.DnsBulkRequest

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsBulk("YOUR_API_KEY", "value", DnsBulkRequest(), null)
    println(result)  // status via api.dnsBulkWithHttpInfo(...).statusCode
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```kotlin
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DomainAvailabilityApi

fun main() {
    val api = DomainAvailabilityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.domainAvailabilityV2("YOUR_API_KEY", "example.com", null, null, null)
    println(result)  // status via api.domainAvailabilityV2WithHttpInfo(...).statusCode
}

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```kotlin
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.api.DomainAvailabilityApi
import com.whoisfreaks.models.BulkDomainAvailabilityRequest

fun main() {
    val api = DomainAvailabilityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkDomainAvailabilityV2("YOUR_API_KEY", BulkDomainAvailabilityRequest(), null, null)
    println(result)  // status via api.bulkDomainAvailabilityV2WithHttpInfo(...).statusCode
}

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```kotlin
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.api.TyposquattingApi

fun main() {
    val api = TyposquattingApi(basePath = "https://api.whoisfreaks.com")
    val result = api.typosquatting("YOUR_API_KEY", null, null, null)
    println(result)  // status via api.typosquattingWithHttpInfo(...).statusCode
}

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```kotlin
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.SSLApi

fun main() {
    val api = SSLApi(basePath = "https://api.whoisfreaks.com")
    val result = api.sslLookup("YOUR_API_KEY", "example.com", null, null, null)
    println(result)  // status via api.sslLookupWithHttpInfo(...).statusCode
}

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```kotlin
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.api.GeolocationApi

fun main() {
    val api = GeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.geolocation("YOUR_API_KEY", "8.8.8.8")
    println(result)  // status via api.geolocationWithHttpInfo(...).statusCode
}

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```kotlin
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.api.GeolocationApi
import com.whoisfreaks.models.BulkGeolocationRequest

fun main() {
    val api = GeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkGeolocation("YOUR_API_KEY", BulkGeolocationRequest())
    println(result)  // status via api.bulkGeolocationWithHttpInfo(...).statusCode
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```kotlin
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.SubdomainsApi

fun main() {
    val api = SubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.subdomains("YOUR_API_KEY", "example.com", "2000-01-01", java.time.LocalDate.now().toString(), null, null, null)
    println(result)  // status via api.subdomainsWithHttpInfo(...).statusCode
}

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```kotlin
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.api.IPReputationApi

fun main() {
    val api = IPReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.ipReputation("YOUR_API_KEY", "8.8.8.8")
    println(result)  // status via api.ipReputationWithHttpInfo(...).statusCode
}

```

#### Bulk IP Reputation

`POST /v1.0/security`

```kotlin
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.api.IPReputationApi
import com.whoisfreaks.models.BulkGeolocationRequest

fun main() {
    val api = IPReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkIpReputation("YOUR_API_KEY", BulkGeolocationRequest())
    println(result)  // status via api.bulkIpReputationWithHttpInfo(...).statusCode
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```kotlin
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DomainReputationApi

fun main() {
    val api = DomainReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.domainReputation("YOUR_API_KEY", "example.com", null)
    println(result)  // status via api.domainReputationWithHttpInfo(...).statusCode
}

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```kotlin
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.ASNWHOISApi

fun main() {
    val api = ASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.asnWhois("YOUR_API_KEY", "AS15169", null)
    println(result)  // status via api.asnWhoisWithHttpInfo(...).statusCode
}

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```kotlin
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.IPWHOISApi

fun main() {
    val api = IPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.ipWhois("YOUR_API_KEY", "8.8.8.8", null)
    println(result)  // status via api.ipWhoisWithHttpInfo(...).statusCode
}

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```kotlin
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.rotateApiKey("YOUR_API_KEY")
    println(result)  // status via api.rotateApiKeyWithHttpInfo(...).statusCode
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```kotlin
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.accountUsage("YOUR_API_KEY")
    println(result)  // status via api.accountUsageWithHttpInfo(...).statusCode
}

```

#### Database File Status (Public)

`GET /v3.3/status`

```kotlin
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import com.whoisfreaks.api.AccountApi

fun main() {
    val api = AccountApi(basePath = "https://api.whoisfreaks.com")
    val result = api.databaseFileStatus()
    println(result)  // status via api.databaseFileStatusWithHttpInfo(...).statusCode
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyGtld("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.dbNewlyGtldWithHttpInfo(...).statusCode
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyCctld("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.dbNewlyCctldWithHttpInfo(...).statusCode
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```kotlin
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyGtldCleaned("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbNewlyGtldCleanedWithHttpInfo(...).statusCode
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```kotlin
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyCctldCleaned("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbNewlyCctldCleanedWithHttpInfo(...).statusCode
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```kotlin
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyGtldJson("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.dbNewlyGtldJsonWithHttpInfo(...).statusCode
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```kotlin
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyCctldJson("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.dbNewlyCctldJsonWithHttpInfo(...).statusCode
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```kotlin
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyDns("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbNewlyDnsWithHttpInfo(...).statusCode
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```kotlin
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbExpired("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbExpiredWithHttpInfo(...).statusCode
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```kotlin
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbExpiredCleaned("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbExpiredCleanedWithHttpInfo(...).statusCode
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```kotlin
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDropped("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDroppedWithHttpInfo(...).statusCode
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```kotlin
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDroppedJson("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null)
    println(result)  // status via api.dbDroppedJsonWithHttpInfo(...).statusCode
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```kotlin
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDroppedBacklinks("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDroppedBacklinksWithHttpInfo(...).statusCode
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```kotlin
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesWHOISApi

fun main() {
    val api = DatabasesWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbWhoisDaily("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbWhoisDailyWithHttpInfo(...).statusCode
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesWHOISApi

fun main() {
    val api = DatabasesWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbWhoisWeekly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbWhoisWeeklyWithHttpInfo(...).statusCode
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```kotlin
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesWHOISApi

fun main() {
    val api = DatabasesWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbWhoisMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbWhoisMonthlyWithHttpInfo(...).statusCode
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```kotlin
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesDNSApi

fun main() {
    val api = DatabasesDNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDnsDaily("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDnsDailyWithHttpInfo(...).statusCode
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```kotlin
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesDNSApi

fun main() {
    val api = DatabasesDNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDnsWeekly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDnsWeeklyWithHttpInfo(...).statusCode
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```kotlin
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesDNSApi

fun main() {
    val api = DatabasesDNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbDnsMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbDnsMonthlyWithHttpInfo(...).statusCode
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```kotlin
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesSubdomainsApi

fun main() {
    val api = DatabasesSubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbSubdomainsDaily("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbSubdomainsDailyWithHttpInfo(...).statusCode
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```kotlin
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesSubdomainsApi

fun main() {
    val api = DatabasesSubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbSubdomainsWeekly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbSubdomainsWeeklyWithHttpInfo(...).statusCode
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```kotlin
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesSubdomainsApi

fun main() {
    val api = DatabasesSubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbSubdomainsMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbSubdomainsMonthlyWithHttpInfo(...).statusCode
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCountryStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpCountryStatusWithHttpInfo(...).statusCode
}

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```kotlin
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCountry("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpCountryWithHttpInfo(...).statusCode
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCityStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpCityStatusWithHttpInfo(...).statusCode
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```kotlin
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPGeolocationApi

fun main() {
    val api = DatabasesIPGeolocationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpCity("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpCityWithHttpInfo(...).statusCode
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesASNWHOISApi

fun main() {
    val api = DatabasesASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbAsnWhois("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbAsnWhoisWithHttpInfo(...).statusCode
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```kotlin
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesASNWHOISApi

fun main() {
    val api = DatabasesASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbAsnWhoisStatus("YOUR_API_KEY")
    println(result)  // status via api.dbAsnWhoisStatusWithHttpInfo(...).statusCode
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPWHOISApi

fun main() {
    val api = DatabasesIPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpWhois("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpWhoisWithHttpInfo(...).statusCode
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```kotlin
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPWHOISApi

fun main() {
    val api = DatabasesIPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpWhoisStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpWhoisStatusWithHttpInfo(...).statusCode
}

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPSecurityApi

fun main() {
    val api = DatabasesIPSecurityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpSecurity("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpSecurityWithHttpInfo(...).statusCode
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```kotlin
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPSecurityApi

fun main() {
    val api = DatabasesIPSecurityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpSecurityStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpSecurityStatusWithHttpInfo(...).statusCode
}

```
