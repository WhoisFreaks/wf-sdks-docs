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

All 54 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

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

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```java
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;
import com.whoisfreaks.client.model.BulkWhoisRequest;

public class BulkWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.bulkWhoisWithHttpInfo("YOUR_API_KEY", new BulkWhoisRequest(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```java
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisHistory {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisHistoryWithHttpInfo("YOUR_API_KEY", "example.com", null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```java
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisReverseWithHttpInfo("YOUR_API_KEY", "value", null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### DNS

#### Live DNS Lookup

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

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```java
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;

public class DnsHistorical {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DnsApi api = new DnsApi(client);
        var resp = api.dnsHistoricalWithHttpInfo("YOUR_API_KEY", "example.com", "value", null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```java
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;

public class DnsReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DnsApi api = new DnsApi(client);
        var resp = api.dnsReverseWithHttpInfo("YOUR_API_KEY", "value", "a", true, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```java
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.model.DnsBulkRequest;

public class DnsBulk {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DnsApi api = new DnsApi(client);
        var resp = api.dnsBulkWithHttpInfo("YOUR_API_KEY", "value", new DnsBulkRequest(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Domain Availability

#### Domain Availability Check with Suggestions

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

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```java
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DomainAvailabilityApi;
import com.whoisfreaks.client.model.BulkDomainAvailabilityRequest;

public class BulkDomainAvailabilityV2 {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DomainAvailabilityApi api = new DomainAvailabilityApi(client);
        var resp = api.bulkDomainAvailabilityV2WithHttpInfo("YOUR_API_KEY", new BulkDomainAvailabilityRequest(), null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Typosquatting

#### Typosquatting Lookup

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

### SSL

#### SSL Certificate Lookup

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

### Geolocation

#### IP Geolocation Lookup

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

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```java
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.model.BulkGeolocationRequest;

public class BulkGeolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        GeolocationApi api = new GeolocationApi(client);
        var resp = api.bulkGeolocationWithHttpInfo("YOUR_API_KEY", new BulkGeolocationRequest());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Subdomains

#### Subdomains Lookup

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

### IP Reputation

#### IP Reputation Lookup

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

#### Bulk IP Reputation

`POST /v1.0/security`

```java
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.model.BulkGeolocationRequest;

public class BulkIpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        IpReputationApi api = new IpReputationApi(client);
        var resp = api.bulkIpReputationWithHttpInfo("YOUR_API_KEY", new BulkGeolocationRequest());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Domain Reputation

#### Domain Reputation Lookup

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

### ASN WHOIS

#### ASN WHOIS Lookup

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

### IP WHOIS

#### IP WHOIS Lookup

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

### Account

#### Rotate API Key

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

#### Account Usage

`GET /v1.0/whoisapi/usage`

```java
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class AccountUsage {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AccountApi api = new AccountApi(client);
        var resp = api.accountUsageWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Database File Status (Public)

`GET /v3.3/status`

```java
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class DatabaseFileStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AccountApi api = new AccountApi(client);
        var resp = api.databaseFileStatusWithHttpInfo();
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

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

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```java
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyCctldWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```java
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyGtldCleanedWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```java
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctldCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyCctldCleanedWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```java
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyGtldJsonWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```java
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyCctldJsonWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```java
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyDns {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyDnsWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Expiring & Dropped

#### Expiring Domains

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

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```java
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbExpiredCleaned {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbExpiredCleanedWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```java
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDropped {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbDroppedWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```java
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDroppedJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbDroppedJsonWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```java
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDroppedBacklinks {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbDroppedBacklinksWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - WHOIS

#### WHOIS Database Daily

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

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```java
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var resp = api.dbWhoisWeeklyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```java
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesWhoisApi;

public class DbWhoisMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesWhoisApi api = new DatabasesWhoisApi(client);
        var resp = api.dbWhoisMonthlyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - DNS

#### DNS Database Daily

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

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```java
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var resp = api.dbDnsWeeklyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```java
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var resp = api.dbDnsMonthlyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - Subdomains

#### Subdomains Daily

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

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```java
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var resp = api.dbSubdomainsWeeklyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```java
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesSubdomainsApi;

public class DbSubdomainsMonthly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesSubdomainsApi api = new DatabasesSubdomainsApi(client);
        var resp = api.dbSubdomainsMonthlyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

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

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```java
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCountry {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var resp = api.dbIpCountryWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var resp = api.dbIpCityStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```java
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var resp = api.dbIpCityWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

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

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```java
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesAsnWhoisApi;

public class DbAsnWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesAsnWhoisApi api = new DatabasesAsnWhoisApi(client);
        var resp = api.dbAsnWhoisStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

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

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```java
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpWhoisApi;

public class DbIpWhoisStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpWhoisApi api = new DatabasesIpWhoisApi(client);
        var resp = api.dbIpWhoisStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Databases - IP Security

#### IP Security Snapshot

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

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```java
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var resp = api.dbIpSecurityStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```
