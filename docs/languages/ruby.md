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

All 55 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

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

### DNS: Live DNS Lookup

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

### Domain Availability: Domain Availability Check with Suggestions

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

### Typosquatting: Typosquatting Lookup

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

### SSL: SSL Certificate Lookup

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

### Geolocation: IP Geolocation Lookup

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

### Subdomains: Subdomains Lookup

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

### IP Reputation: IP Reputation Lookup

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

### Domain Reputation: Domain Reputation Lookup

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

### ASN WHOIS: ASN WHOIS Lookup

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

### IP WHOIS: IP WHOIS Lookup

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

### Account: Rotate API Key

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

### Databases - Newly Registered: Newly Registered gTLD (CSV)

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

### Databases - Expiring & Dropped: Expiring Domains

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

### Databases - WHOIS: WHOIS Database Daily

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

### Databases - DNS: DNS Database Daily

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

### Databases - Subdomains: Subdomains Daily

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

### Databases - IP Geolocation: IP to Country Snapshot Status

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

### Databases - ASN WHOIS: ASN WHOIS Snapshot

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

### Databases - IP WHOIS: IP WHOIS Snapshot

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

### Databases - IP Security: IP Security Snapshot

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
