# PHP SDK

## About

The official **WhoisFreaks PHP SDK** — a complete client for WHOIS, DNS, SSL, domain availability, subdomain, IP geolocation, IP reputation, ASN, typosquatting, and domain reputation lookups, plus bulk database downloads. Query real-time and historical domain data, reverse WHOIS, and threat intelligence from PHP with a single API key. Generated from the WhoisFreaks OpenAPI specification and published to Packagist.

**Keywords:** php whois api, php whois sdk, whoisfreaks php, php domain lookup, php dns api, whois api, whois lookup, domain api, dns api, dns lookup, reverse whois, historical whois, domain availability api, ssl certificate api, ip geolocation api, ip reputation api, asn lookup, subdomain finder, typosquatting api, domain reputation, threat intelligence api, domain data api, whois sdk, domain monitoring, brand protection api

- **Registry:** Packagist
- **Package:** `WhoisFreaks/whoisfreaks-php`

## Install

```bash
composer require WhoisFreaks/whoisfreaks-php
```

## Build from Source

Prefer to build the SDK yourself instead of installing from Packagist? Clone the monorepo and build the PHP package locally:

```bash
git clone https://github.com/WhoisFreaks/whoisfreaks-php
cd whoisfreaks-php
composer install
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
composer init --no-interaction
composer require WhoisFreaks/whoisfreaks-php
```

Create `main.php`:

```php
<?php
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");   // set once
$api = new WhoisFreaks\Api\WhoisApi(new GuzzleHttp\Client(), $config);
$result = $api->whoisLive("example.com");
print_r($result);
```

Run it:

```bash
php main.php
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```php
<?php
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->whoisLive("example.com", null);
print_r($result);

```

## Endpoints

All 60 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```php
<?php
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->whoisLive("example.com", null);
print_r($result);

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```php
<?php
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkWhois(new WhoisFreaks\Model\BulkWhoisRequest(), null);
print_r($result);

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```php
<?php
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->whoisHistory("example.com", null, null);
print_r($result);

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```php
<?php
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->whoisReverse("value", null, null);
print_r($result);

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```php
<?php
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dnsLive("example.com", "8.8.8.8", "value", null);
print_r($result);

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```php
<?php
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dnsHistorical("example.com", "value", null, null);
print_r($result);

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```php
<?php
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dnsReverse("value", "a", true, null, null);
print_r($result);

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```php
<?php
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dnsBulk("value", new WhoisFreaks\Model\DnsBulkRequest(), null);
print_r($result);

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```php
<?php
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
$result = $api->domainAvailabilityV2("example.com", null, null, null);
print_r($result);

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```php
<?php
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkDomainAvailabilityV2(new WhoisFreaks\Model\BulkDomainAvailabilityRequest(), null, null);
print_r($result);

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```php
<?php
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\TyposquattingApi(new GuzzleHttp\Client(), $config);
$result = $api->typosquatting(null, null, null);
print_r($result);

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```php
<?php
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\SSLApi(new GuzzleHttp\Client(), $config);
$result = $api->sslLookup("example.com", null, null, null);
print_r($result);

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```php
<?php
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->geolocation("8.8.8.8");
print_r($result);

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```php
<?php
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkGeolocation(new WhoisFreaks\Model\BulkGeolocationRequest());
print_r($result);

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```php
<?php
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\SubdomainsApi(new GuzzleHttp\Client(), $config);
$result = $api->subdomains("example.com", "2000-01-01", (new DateTime("today"))->format("Y-m-d"), null, null, null);
print_r($result);

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```php
<?php
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
$result = $api->ipReputation("8.8.8.8");
print_r($result);

```

#### Bulk IP Reputation

`POST /v1.0/security`

```php
<?php
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkIpReputation(new WhoisFreaks\Model\BulkIpReputationRequest());
print_r($result);

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```php
<?php
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DomainReputationApi(new GuzzleHttp\Client(), $config);
$result = $api->domainReputation("example.com", null);
print_r($result);

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```php
<?php
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\ASNWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->asnWhois("AS15169", null);
print_r($result);

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```php
<?php
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\IPWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->ipWhois("8.8.8.8", null);
print_r($result);

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```php
<?php
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
$result = $api->rotateApiKey();
print_r($result);

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```php
<?php
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
$result = $api->accountUsage();
print_r($result);

```

#### Database File Status (Public)

`GET /v3.4/status`

```php
<?php
// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
$result = $api->databaseFileStatus();
print_r($result);

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```php
<?php
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyGtld(false, (new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```php
<?php
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyCctld(false, (new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```php
<?php
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyGtldCleaned((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```php
<?php
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyCctldCleaned((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```php
<?php
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyGtldJson((new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```php
<?php
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyCctldJson((new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```php
<?php
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyDns((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```php
<?php
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbExpired(false, (new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```php
<?php
// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbExpiredCleaned((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```php
<?php
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDropped(false, (new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```php
<?php
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDroppedJson((new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```php
<?php
// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDroppedBacklinks(false, (new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```php
<?php
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbWhoisDaily((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```php
<?php
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbWhoisWeekly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```php
<?php
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbWhoisMonthly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```php
<?php
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesDNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDnsDaily((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```php
<?php
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesDNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDnsWeekly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```php
<?php
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesDNSApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDnsMonthly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```php
<?php
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesSubdomainsApi(new GuzzleHttp\Client(), $config);
$result = $api->dbSubdomainsDaily((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```php
<?php
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesSubdomainsApi(new GuzzleHttp\Client(), $config);
$result = $api->dbSubdomainsWeekly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```php
<?php
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesSubdomainsApi(new GuzzleHttp\Client(), $config);
$result = $api->dbSubdomainsMonthly((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```php
<?php
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpCountryStatus();
print_r($result);

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```php
<?php
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpCountry((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```php
<?php
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpCityStatus();
print_r($result);

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```php
<?php
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpCity((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```php
<?php
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesASNWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbAsnWhois((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```php
<?php
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesASNWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbAsnWhoisStatus();
print_r($result);

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```php
<?php
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpWhois((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```php
<?php
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpWhoisStatus();
print_r($result);

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```php
<?php
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPSecurityApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpSecurity((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```php
<?php
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPSecurityApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpSecurityStatus();
print_r($result);

```

### Databases - Threat Feed

#### Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

```php
<?php
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedPhishing((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

```php
<?php
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedPhishingSample();
print_r($result);

```

#### Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

```php
<?php
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedMalware((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

```php
<?php
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedMalwareSample();
print_r($result);

```

#### Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

```php
<?php
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedSpam((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);

```

#### Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

```php
<?php
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedSpamSample();
print_r($result);

```
