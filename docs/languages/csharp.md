# C# / .NET SDK

- **Registry:** NuGet
- **Package:** `WhoisFreaks`

## Install

```bash
dotnet add package WhoisFreaks
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
dotnet new console
dotnet add package WhoisFreaks
```

Replace `Program.cs` with:

```csharp
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
var api = new WHOISApi(config);

var resp = api.WhoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
Console.WriteLine($"status: {(int)resp.StatusCode}");
Console.WriteLine(resp.Data);
```

Run it:

```bash
dotnet run
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class WhoisLive {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new WHOISApi(config);
        var resp = api.WhoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

## Endpoints

All 55 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

`GET /v2.0/whois/live`

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class WhoisLive {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new WHOISApi(config);
        var resp = api.WhoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### DNS: Live DNS Lookup

`GET /v2.0/dns/live`

```csharp
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DnsLive {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DNSApi(config);
        var resp = api.DnsLiveWithHttpInfo("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Domain Availability: Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```csharp
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DomainAvailabilityV2 {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DomainAvailabilityApi(config);
        var resp = api.DomainAvailabilityV2WithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Typosquatting: Typosquatting Lookup

`GET /v3.0/domain/typos`

```csharp
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Typosquatting {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new TyposquattingApi(config);
        var resp = api.TyposquattingWithHttpInfo("YOUR_API_KEY", null, null, null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### SSL: SSL Certificate Lookup

`GET /v1.0/ssl/live`

```csharp
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class SslLookup {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new SSLApi(config);
        var resp = api.SslLookupWithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```csharp
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Geolocation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new GeolocationApi(config);
        var resp = api.GeolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Subdomains: Subdomains Lookup

`GET /v1.0/subdomains`

```csharp
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Subdomains {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new SubdomainsApi(config);
        var resp = api.SubdomainsWithHttpInfo("YOUR_API_KEY", "example.com", "2000-01-01", DateTime.UtcNow.ToString("yyyy-MM-dd"), null, null, null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```csharp
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class IpReputation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new IPReputationApi(config);
        var resp = api.IpReputationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```csharp
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DomainReputation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DomainReputationApi(config);
        var resp = api.DomainReputationWithHttpInfo("YOUR_API_KEY", "example.com", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```csharp
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class AsnWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new ASNWHOISApi(config);
        var resp = api.AsnWhoisWithHttpInfo("YOUR_API_KEY", "AS15169", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```csharp
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class IpWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new IPWHOISApi(config);
        var resp = api.IpWhoisWithHttpInfo("YOUR_API_KEY", "8.8.8.8", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```csharp
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class RotateApiKey {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new AccountApi(config);
        var resp = api.RotateApiKeyWithHttpInfo("YOUR_API_KEY");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - Newly Registered: Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```csharp
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbNewlyGtld {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesNewlyRegisteredApi(config);
        var resp = api.DbNewlyGtldWithHttpInfo("YOUR_API_KEY", false, DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"), null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```csharp
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbExpired {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesExpiringDroppedApi(config);
        var resp = api.DbExpiredWithHttpInfo("YOUR_API_KEY", false, DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```csharp
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbWhoisDaily {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesWHOISApi(config);
        var resp = api.DbWhoisDailyWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```csharp
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbDnsDaily {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesDNSApi(config);
        var resp = api.DbDnsDailyWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```csharp
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbSubdomainsDaily {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesSubdomainsApi(config);
        var resp = api.DbSubdomainsDailyWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```csharp
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpCountryStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesIPGeolocationApi(config);
        var resp = api.DbIpCountryStatusWithHttpInfo("YOUR_API_KEY");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```csharp
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbAsnWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesASNWHOISApi(config);
        var resp = api.DbAsnWhoisWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```csharp
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesIPWHOISApi(config);
        var resp = api.DbIpWhoisWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```csharp
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpSecurity {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesIPSecurityApi(config);
        var resp = api.DbIpSecurityWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```
