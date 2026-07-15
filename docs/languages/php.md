# PHP SDK

- **Registry:** Packagist
- **Package:** `WhoisFreaks/whoisfreaks-php`

## Install

```bash
composer require WhoisFreaks/whoisfreaks-php
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

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WhoisApi(new GuzzleHttp\Client(), $config);
list($data, $status, $headers) = $api->whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $status . PHP_EOL;
print_r($data);
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
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

## Endpoints

All 55 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

`GET /v2.0/whois/live`

```php
<?php
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### DNS: Live DNS Lookup

`GET /v2.0/dns/live`

```php
<?php
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dnsLiveWithHttpInfo("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Domain Availability: Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```php
<?php
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->domainAvailabilityV2WithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Typosquatting: Typosquatting Lookup

`GET /v3.0/domain/typos`

```php
<?php
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\TyposquattingApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->typosquattingWithHttpInfo("YOUR_API_KEY", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### SSL: SSL Certificate Lookup

`GET /v1.0/ssl/live`

```php
<?php
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\SSLApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->sslLookupWithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Geolocation: IP Geolocation Lookup

`GET /v1.0/geolocation`

```php
<?php
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->geolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Subdomains: Subdomains Lookup

`GET /v1.0/subdomains`

```php
<?php
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\SubdomainsApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->subdomainsWithHttpInfo("YOUR_API_KEY", "example.com", "2000-01-01", (new DateTime("today"))->format("Y-m-d"), null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### IP Reputation: IP Reputation Lookup

`GET /v1.0/security`

```php
<?php
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->ipReputationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Domain Reputation: Domain Reputation Lookup

`GET /v1/domain/security`

```php
<?php
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DomainReputationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->domainReputationWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### ASN WHOIS: ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```php
<?php
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\ASNWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->asnWhoisWithHttpInfo("YOUR_API_KEY", "AS15169", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### IP WHOIS: IP WHOIS Lookup

`GET /v1.0/ip-whois`

```php
<?php
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\IPWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->ipWhoisWithHttpInfo("YOUR_API_KEY", "8.8.8.8", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Account: Rotate API Key

`GET /v1.0/api-key/rotate`

```php
<?php
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->rotateApiKeyWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - Newly Registered: Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```php
<?php
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbNewlyGtldWithHttpInfo("YOUR_API_KEY", false, (new DateTime("yesterday"))->format("Y-m-d"), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - Expiring & Dropped: Expiring Domains

`GET /v3.1/download/domainer/expired`

```php
<?php
// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbExpiredWithHttpInfo("YOUR_API_KEY", false, (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - WHOIS: WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```php
<?php
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbWhoisDailyWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - DNS: DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```php
<?php
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesDNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbDnsDailyWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - Subdomains: Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```php
<?php
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesSubdomainsApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbSubdomainsDailyWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - IP Geolocation: IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```php
<?php
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpCountryStatusWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - ASN WHOIS: ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```php
<?php
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesASNWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbAsnWhoisWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - IP WHOIS: IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```php
<?php
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpWhoisWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```

### Databases - IP Security: IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```php
<?php
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPSecurityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpSecurityWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```
