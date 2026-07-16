# Ruby SDK

- **Registry:** RubyGems
- **Package:** `whoisfreaks`

## Install

```bash
gem install whoisfreaks
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
gem install whoisfreaks
```

Create `main.rb`:

```ruby
require 'whoisfreaks'

api = WhoisFreaks::WhoisApi.new
data, status, _headers = api.whois_live_with_http_info(api_key: "YOUR_API_KEY", domain_name: "example.com")
puts "status: #{status}"
puts data
```

Run it:

```bash
ruby main.rb
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```ruby
# Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_live_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

## Endpoints

All 55 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```ruby
# Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_live_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

#### WHOIS Historical or Reverse Lookup

`GET /v1.0/whois`

```ruby
# Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
# Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (string (one of: historical, reverse), required)
#   - domainName (string, required): Required for historical lookup
#   - keyword (string, optional): For reverse — domain keyword search
#   - email (string, optional): For reverse — registrant email search
#   - owner (string, optional): For reverse — registrant name search
#   - company (string, optional): For reverse — company name search
#   - mode (string (one of: default, mini), optional)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_historical_or_reverse_with_http_info("YOUR_API_KEY", "historical", "example.com", true)
puts "status: #{status}"
puts data

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```ruby
# Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.bulk_whois_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkWhoisRequest.new)
puts "status: #{status}"
puts data

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```ruby
# Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_history_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```ruby
# Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_reverse_with_http_info("YOUR_API_KEY", "value")
puts "status: #{status}"
puts data

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```ruby
# Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
# Parameters for dnsLive (GET /v2.0/dns/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_live_with_http_info("YOUR_API_KEY", "example.com", "8.8.8.8", "value")
puts "status: #{status}"
puts data

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```ruby
# Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_historical_with_http_info("YOUR_API_KEY", "example.com", "value")
puts "status: #{status}"
puts data

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```ruby
# Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_reverse_with_http_info("YOUR_API_KEY", "value", "a", true)
puts "status: #{status}"
puts data

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```ruby
# Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_bulk_with_http_info("YOUR_API_KEY", "value", WhoisFreaks::DnsBulkRequest.new)
puts "status: #{status}"
puts data

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```ruby
# Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DomainAvailabilityApi.new
data, status, _headers = api.domain_availability_v2_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```ruby
# Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::DomainAvailabilityApi.new
data, status, _headers = api.bulk_domain_availability_v2_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkDomainAvailabilityRequest.new)
puts "status: #{status}"
puts data

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```ruby
# Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
require 'whoisfreaks'

api = WhoisFreaks::TyposquattingApi.new
data, status, _headers = api.typosquatting_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```ruby
# Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::SSLApi.new
data, status, _headers = api.ssl_lookup_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```ruby
# Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
# Parameters for geolocation (GET /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
require 'whoisfreaks'

api = WhoisFreaks::GeolocationApi.new
data, status, _headers = api.geolocation_with_http_info("YOUR_API_KEY", "8.8.8.8")
puts "status: #{status}"
puts data

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```ruby
# Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::GeolocationApi.new
data, status, _headers = api.bulk_geolocation_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkGeolocationRequest.new)
puts "status: #{status}"
puts data

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```ruby
# Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
# Parameters for subdomains (GET /v1.0/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::SubdomainsApi.new
data, status, _headers = api.subdomains_with_http_info("YOUR_API_KEY", "example.com", "2000-01-01", Date.today.to_s)
puts "status: #{status}"
puts data

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```ruby
# Runnable example: IP Reputation Lookup (GET /v1.0/security)
# Parameters for ipReputation (GET /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
require 'whoisfreaks'

api = WhoisFreaks::IPReputationApi.new
data, status, _headers = api.ip_reputation_with_http_info("YOUR_API_KEY", "8.8.8.8")
puts "status: #{status}"
puts data

```

#### Bulk IP Reputation

`POST /v1.0/security`

```ruby
# Runnable example: Bulk IP Reputation (POST /v1.0/security)
# Parameters for bulkIpReputation (POST /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::IPReputationApi.new
data, status, _headers = api.bulk_ip_reputation_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkGeolocationRequest.new)
puts "status: #{status}"
puts data

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```ruby
# Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
# Parameters for domainReputation (GET /v1/domain/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DomainReputationApi.new
data, status, _headers = api.domain_reputation_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```ruby
# Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::ASNWHOISApi.new
data, status, _headers = api.asn_whois_with_http_info("YOUR_API_KEY", "AS15169")
puts "status: #{status}"
puts data

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```ruby
# Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::IPWHOISApi.new
data, status, _headers = api.ip_whois_with_http_info("YOUR_API_KEY", "8.8.8.8")
puts "status: #{status}"
puts data

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```ruby
# Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.rotate_api_key_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```ruby
# Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.account_usage_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

#### Database File Status (Public)

`GET /v3.3/status`

```ruby
# Runnable example: Database File Status (Public) (GET /v3.3/status)
# Parameters for databaseFileStatus (GET /v3.3/status):
#   (no parameters besides apiKey)
require 'whoisfreaks'

api = WhoisFreaks::AccountApi.new
data, status, _headers = api.database_file_status_with_http_info()
puts "status: #{status}"
puts data

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```ruby
# Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_gtld_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```ruby
# Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
# Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_cctld_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```ruby
# Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_gtld_cleaned_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```ruby
# Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
# Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_cctld_cleaned_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```ruby
# Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_gtld_json_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```ruby
# Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_cctld_json_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```ruby
# Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_dns_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```ruby
# Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_expired_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```ruby
# Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_expired_cleaned_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```ruby
# Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```ruby
# Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_json_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```ruby
# Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_backlinks_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```ruby
# Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
# Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesWHOISApi.new
data, status, _headers = api.db_whois_daily_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```ruby
# Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesWHOISApi.new
data, status, _headers = api.db_whois_weekly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```ruby
# Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesWHOISApi.new
data, status, _headers = api.db_whois_monthly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```ruby
# Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_daily_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```ruby
# Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_weekly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```ruby
# Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_monthly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```ruby
# Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
# Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesSubdomainsApi.new
data, status, _headers = api.db_subdomains_daily_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```ruby
# Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesSubdomainsApi.new
data, status, _headers = api.db_subdomains_weekly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```ruby
# Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
# Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesSubdomainsApi.new
data, status, _headers = api.db_subdomains_monthly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```ruby
# Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_country_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```ruby
# Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_country_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```ruby
# Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_city_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```ruby
# Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_city_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```ruby
# Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesASNWHOISApi.new
data, status, _headers = api.db_asn_whois_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```ruby
# Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesASNWHOISApi.new
data, status, _headers = api.db_asn_whois_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```ruby
# Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPWHOISApi.new
data, status, _headers = api.db_ip_whois_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```ruby
# Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPWHOISApi.new
data, status, _headers = api.db_ip_whois_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```ruby
# Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPSecurityApi.new
data, status, _headers = api.db_ip_security_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```ruby
# Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPSecurityApi.new
data, status, _headers = api.db_ip_security_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data

```
