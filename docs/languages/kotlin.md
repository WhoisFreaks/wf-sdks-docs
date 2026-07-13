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

All 53 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

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

### DNS: Live DNS Lookup

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

### Domain Availability: Domain Availability Check with Suggestions

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

### Typosquatting: Typosquatting Lookup

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

### SSL: SSL Certificate Lookup

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

### Geolocation: IP Geolocation Lookup

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

### Subdomains: Subdomains Lookup

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

### IP Reputation: IP Reputation Lookup

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

### Domain Reputation: Domain Reputation Lookup

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

### ASN WHOIS: ASN WHOIS Lookup

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

### IP WHOIS: IP WHOIS Lookup

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

### Account: Rotate API Key

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

### Databases - Newly Registered: Newly Registered gTLD (CSV)

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

### Databases - Expiring & Dropped: Expiring Domains

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

### Databases - WHOIS: WHOIS Database Daily

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

### Databases - DNS: DNS Database Daily

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

### Databases - Subdomains: Subdomains Daily

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

### Databases - IP Geolocation: IP to Country Snapshot Status

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

### Databases - ASN WHOIS: ASN WHOIS Snapshot

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

### Databases - IP WHOIS: IP WHOIS Snapshot

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

### Databases - IP Security: IP Security Snapshot

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
