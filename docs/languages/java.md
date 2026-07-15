# Java SDK

- **Registry:** Maven Central
- **Package:** `com.whoisfreaks:whoisfreaks`

## Install

```xml
<dependency>
  <groupId>com.whoisfreaks</groupId>
  <artifactId>whoisfreaks</artifactId>
  <version>LATEST</version>
</dependency>
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

Create a Maven project and add the dependency to `pom.xml`:

```xml
<dependency>
  <groupId>com.whoisfreaks</groupId>
  <artifactId>whoisfreaks</artifactId>
  <version>LATEST</version>   <!-- pin to a real version, e.g. 1.0.0 -->
</dependency>
```

`src/main/java/Main.java`:

```java
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class Main {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
```

Build and run with `mvn compile exec:java -Dexec.mainClass=Main` (or your IDE).

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

## Endpoints

All 55 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

`GET /v2.0/whois/live`

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### DNS: Live DNS Lookup

`GET /v2.0/dns/live`

```java
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;

public class DnsLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DnsApi api = new DnsApi(client);
        var resp = api.dnsLiveWithHttpInfo("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Domain Availability: Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```java
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainAvailabilityApi;

public class DomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);
        var resp = api.domainAvailabilityV2WithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Typosquatting: Typosquatting Lookup

`GET /v3.0/domain/typos`

```java
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.TyposquattingApi;

public class Typosquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        TyposquattingApi api = new TyposquattingApi(client);
        var resp = api.typosquattingWithHttpInfo("YOUR_API_KEY", null, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### SSL: SSL Certificate Lookup

`GET /v1.0/ssl/live`

```java
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SslApi;

public class SslLookup {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        SslApi api = new SslApi(client);
        var resp = api.sslLookupWithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```java
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        GeolocationApi api = new GeolocationApi(client);
        var resp = api.geolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Subdomains: Subdomains Lookup

`GET /v1.0/subdomains`

```java
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.SubdomainsApi;

public class Subdomains {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        SubdomainsApi api = new SubdomainsApi(client);
        var resp = api.subdomainsWithHttpInfo("YOUR_API_KEY", "example.com", "2000-01-01", java.time.LocalDate.now().toString(), null, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```java
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;

public class IpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        IpReputationApi api = new IpReputationApi(client);
        var resp = api.ipReputationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```java
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainReputationApi;

public class DomainReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DomainReputationApi api = new DomainReputationApi(client);
        var resp = api.domainReputationWithHttpInfo("YOUR_API_KEY", "example.com", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```java
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AsnWhoisApi;

public class AsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AsnWhoisApi api = new AsnWhoisApi(client);
        var resp = api.asnWhoisWithHttpInfo("YOUR_API_KEY", "AS15169", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```java
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpWhoisApi;

public class IpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        IpWhoisApi api = new IpWhoisApi(client);
        var resp = api.ipWhoisWithHttpInfo("YOUR_API_KEY", "8.8.8.8", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```java
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class RotateApiKey {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AccountApi api = new AccountApi(client);
        var resp = api.rotateApiKeyWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Newly Registered: Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```java
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyGtldWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```java
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbExpired {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbExpiredWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```java
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var resp = api.dbWhoisDailyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```java
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var resp = api.dbDnsDailyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```java
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var resp = api.dbSubdomainsDailyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCountryStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var resp = api.dbIpCountryStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;

public class DbAsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);
        var resp = api.dbAsnWhoisWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;

public class DbIpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);
        var resp = api.dbIpWhoisWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var resp = api.dbIpSecurityWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```
