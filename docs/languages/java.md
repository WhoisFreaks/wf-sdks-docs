# Java SDK

## About

The official **WhoisFreaks Java SDK** — a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from Java with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Maven Central.

**Keywords:** java whois api, java whois sdk, whoisfreaks java, java domain lookup, java dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

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

## Build from Source

Prefer to build the SDK yourself instead of installing from Maven Central? Clone the monorepo and build the Java package locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-java
cd whoisfreaks-java
mvn clean install   # builds + installs to local ~/.m2
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
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;

public class Main {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.whoisLive("example.com");
        System.out.println(result);
    }
}
```

Build and run with `mvn compile exec:java -Dexec.mainClass=Main` (or your IDE).

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.whoisLive("example.com", null);
        System.out.println(result);
    }
}

```

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.whoisLive("example.com", null);
        System.out.println(result);
    }
}

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```java
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.model.BulkWhoisRequest;

public class BulkWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.bulkWhois(new BulkWhoisRequest(), null);
        System.out.println(result);
    }
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```java
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisHistory {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.whoisHistory("example.com", null, null);
        System.out.println(result);
    }
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```java
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        WhoisApi api = new WhoisApi(client);
        var result = api.whoisReverse("value", null, null);
        System.out.println(result);
    }
}

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```java
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DnsApi;

public class DnsLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DnsApi api = new DnsApi(client);
        var result = api.dnsLive("example.com", "8.8.8.8", "value", null);
        System.out.println(result);
    }
}

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```java
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DnsApi;

public class DnsHistorical {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DnsApi api = new DnsApi(client);
        var result = api.dnsHistorical("example.com", "value", null, null);
        System.out.println(result);
    }
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```java
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DnsApi;

public class DnsReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DnsApi api = new DnsApi(client);
        var result = api.dnsReverse("value", "a", true, null, null);
        System.out.println(result);
    }
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```java
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.model.DnsBulkRequest;

public class DnsBulk {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DnsApi api = new DnsApi(client);
        var result = api.dnsBulk("value", new DnsBulkRequest(), null);
        System.out.println(result);
    }
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```java
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DomainAvailabilityApi;

public class DomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);
        var result = api.domainAvailabilityV2("example.com", null, null, null);
        System.out.println(result);
    }
}

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```java
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DomainAvailabilityApi;
import com.whoisfreaks.client.model.BulkDomainAvailabilityRequest;

public class BulkDomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);
        var result = api.bulkDomainAvailabilityV2(new BulkDomainAvailabilityRequest(), null, null);
        System.out.println(result);
    }
}

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```java
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.TyposquattingApi;

public class Typosquatting {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        TyposquattingApi api = new TyposquattingApi(client);
        var result = api.typosquatting(null, null, null);
        System.out.println(result);
    }
}

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```java
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.SslApi;

public class SslLookup {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        SslApi api = new SslApi(client);
        var result = api.sslLookup("example.com", null, null, null);
        System.out.println(result);
    }
}

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```java
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.GeolocationApi;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        GeolocationApi api = new GeolocationApi(client);
        var result = api.geolocation("8.8.8.8");
        System.out.println(result);
    }
}

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```java
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.model.BulkGeolocationRequest;

public class BulkGeolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        GeolocationApi api = new GeolocationApi(client);
        var result = api.bulkGeolocation(new BulkGeolocationRequest());
        System.out.println(result);
    }
}

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```java
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.SubdomainsApi;

public class Subdomains {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        SubdomainsApi api = new SubdomainsApi(client);
        var result = api.subdomains("example.com", "2000-01-01", java.time.LocalDate.now().toString(), null, null, null);
        System.out.println(result);
    }
}

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```java
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.IpReputationApi;

public class IpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        IpReputationApi api = new IpReputationApi(client);
        var result = api.ipReputation("8.8.8.8");
        System.out.println(result);
    }
}

```

#### Bulk IP Reputation

`POST /v1.0/security`

```java
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.model.BulkIpReputationRequest;

public class BulkIpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        IpReputationApi api = new IpReputationApi(client);
        var result = api.bulkIpReputation(new BulkIpReputationRequest());
        System.out.println(result);
    }
}

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```java
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DomainReputationApi;

public class DomainReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DomainReputationApi api = new DomainReputationApi(client);
        var result = api.domainReputation("example.com", null);
        System.out.println(result);
    }
}

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```java
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.AsnWhoisApi;

public class AsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        AsnWhoisApi api = new AsnWhoisApi(client);
        var result = api.asnWhois("AS15169", null);
        System.out.println(result);
    }
}

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```java
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.IpWhoisApi;

public class IpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        IpWhoisApi api = new IpWhoisApi(client);
        var result = api.ipWhois("8.8.8.8", null);
        System.out.println(result);
    }
}

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```java
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.AccountApi;

public class RotateApiKey {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        AccountApi api = new AccountApi(client);
        var result = api.rotateApiKey();
        System.out.println(result);
    }
}

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```java
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.AccountApi;

public class AccountUsage {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        AccountApi api = new AccountApi(client);
        var result = api.accountUsage();
        System.out.println(result);
    }
}

```

#### Database File Status (Public)

`GET /v3.4/status`

```java
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.AccountApi;

public class DatabaseFileStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        AccountApi api = new AccountApi(client);
        var result = api.databaseFileStatus();
        System.out.println(result);
    }
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```java
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyGtld(false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```java
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyCctld(false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```java
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyGtldCleaned(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```java
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyCctldCleaned(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```java
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyGtldJson(java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```java
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyCctldJson(java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```java
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyDns {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyDns(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```java
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbExpired {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var result = api.dbExpired(false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```java
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbExpiredCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var result = api.dbExpiredCleaned(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```java
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDropped {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var result = api.dbDropped(false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```java
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDroppedJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var result = api.dbDroppedJson(java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```java
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDroppedBacklinks {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var result = api.dbDroppedBacklinks(false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```java
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var result = api.dbWhoisDaily(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```java
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var result = api.dbWhoisWeekly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```java
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var result = api.dbWhoisMonthly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```java
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var result = api.dbDnsDaily(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```java
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var result = api.dbDnsWeekly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```java
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var result = api.dbDnsMonthly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```java
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsDaily {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var result = api.dbSubdomainsDaily(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```java
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var result = api.dbSubdomainsWeekly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```java
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var result = api.dbSubdomainsMonthly(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCountryStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var result = api.dbIpCountryStatus();
        System.out.println(result);
    }
}

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCountry {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var result = api.dbIpCountry(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var result = api.dbIpCityStatus();
        System.out.println(result);
    }
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var result = api.dbIpCity(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;

public class DbAsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);
        var result = api.dbAsnWhois(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;

public class DbAsnWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);
        var result = api.dbAsnWhoisStatus();
        System.out.println(result);
    }
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;

public class DbIpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);
        var result = api.dbIpWhois(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;

public class DbIpWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);
        var result = api.dbIpWhoisStatus();
        System.out.println(result);
    }
}

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var result = api.dbIpSecurity(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var result = api.dbIpSecurityStatus();
        System.out.println(result);
    }
}

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```java
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedPhishing {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedPhishing(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```java
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedPhishingSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedPhishingSample();
        System.out.println(result);
    }
}

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```java
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedMalware {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedMalware(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```java
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedMalwareSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedMalwareSample();
        System.out.println(result);
    }
}

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```java
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedSpam {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedSpam(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```java
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedSpamSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedSpamSample();
        System.out.println(result);
    }
}

```
