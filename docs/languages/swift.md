# Swift SDK

- **Registry:** Swift PM
- **Package:** `github.com/WhoisFreaks/whoisfreaks-swift`

## Install

```swift
.package(url: "https://github.com/WhoisFreaks/whoisfreaks-swift.git", from: "LATEST")
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
swift package init --type executable
```

Add the dependency to `Package.swift`:

```swift
.package(url: "https://github.com/WhoisFreaks/whoisfreaks-swift.git", from: "1.0.0"),
```

…and list `WhoisFreaks` as a target dependency. Then in `Sources/.../main.swift`:

```swift
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com")
    print(result)
} catch {
    print(error)
}
```

Run it:

```bash
swift run
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```swift
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}

```

## Endpoints

All 53 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

`GET /v2.0/whois/live`

```swift
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}

```

### DNS: Live DNS Lookup

`GET /v2.0/dns/live`

```swift
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DNSAPI.dnsLive(apiKey: "YOUR_API_KEY", domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: nil)
    print(result)
} catch {
    print(error)
}

```

### Domain Availability: Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```swift
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DomainAvailabilityAPI.domainAvailabilityV2(apiKey: "YOUR_API_KEY", domain: "example.com", sug: nil, count: nil, format: nil)
    print(result)
} catch {
    print(error)
}

```

### Typosquatting: Typosquatting Lookup

`GET /v3.0/domain/typos`

```swift
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import WhoisFreaks

do {
    let result = try await TyposquattingAPI.typosquatting(apiKey: "YOUR_API_KEY", keyword: nil, pattern: nil, pageToken: nil)
    print(result)
} catch {
    print(error)
}

```

### SSL: SSL Certificate Lookup

`GET /v1.0/ssl/live`

```swift
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await SSLAPI.sslLookup(apiKey: "YOUR_API_KEY", domainName: "example.com", chain: nil, sslRaw: nil, format: nil)
    print(result)
} catch {
    print(error)
}

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```swift
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

do {
    let result = try await GeolocationAPI.geolocation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8")
    print(result)
} catch {
    print(error)
}

```

### Subdomains: Subdomains Lookup

`GET /v1.0/subdomains`

```swift
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import Foundation
import WhoisFreaks

do {
    let result = try await SubdomainsAPI.subdomains(apiKey: "YOUR_API_KEY", domain: "example.com", after: "2000-01-01", before: String(ISO8601DateFormatter().string(from: Date()).prefix(10)), status: nil, page: nil, format: nil)
    print(result)
} catch {
    print(error)
}

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```swift
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import WhoisFreaks

do {
    let result = try await IPReputationAPI.ipReputation(apiKey: "YOUR_API_KEY", ip: "8.8.8.8")
    print(result)
} catch {
    print(error)
}

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```swift
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await DomainReputationAPI.domainReputation(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```swift
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await ASNWHOISAPI.asnWhois(apiKey: "YOUR_API_KEY", asn: "AS15169", format: nil)
    print(result)
} catch {
    print(error)
}

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```swift
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await IPWHOISAPI.ipWhois(apiKey: "YOUR_API_KEY", ip: "8.8.8.8", format: nil)
    print(result)
} catch {
    print(error)
}

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```swift
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await AccountAPI.rotateApiKey(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}

```

### Databases - Newly Registered: Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```swift
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesNewlyRegisteredAPI.dbNewlyGtld(apiKey: "YOUR_API_KEY", whois: false, date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)), tlds: nil)
    print(result)
} catch {
    print(error)
}

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```swift
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesExpiringDroppedAPI.dbExpired(apiKey: "YOUR_API_KEY", whois: false, date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```swift
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesWHOISAPI.dbWhoisDaily(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```swift
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesDNSAPI.dbDnsDaily(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```swift
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesSubdomainsAPI.dbSubdomainsDaily(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```swift
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import WhoisFreaks

do {
    let result = try await DatabasesIPGeolocationAPI.dbIpCountryStatus(apiKey: "YOUR_API_KEY")
    print(result)
} catch {
    print(error)
}

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```swift
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesASNWHOISAPI.dbAsnWhois(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```swift
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesIPWHOISAPI.dbIpWhois(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```swift
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import Foundation
import WhoisFreaks

do {
    let result = try await DatabasesIPSecurityAPI.dbIpSecurity(apiKey: "YOUR_API_KEY", date: String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10)))
    print(result)
} catch {
    print(error)
}

```
