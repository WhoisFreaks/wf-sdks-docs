# Python SDK

- **Registry:** PyPI
- **Package:** `whoisfreaks`

## Install

```bash
pip install whoisfreaks
```

## Getting Started

A complete walkthrough from an empty directory to a running program:

```bash
mkdir whoisfreaks-test && cd whoisfreaks-test
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install whoisfreaks
```

Create `main.py`:

```python
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

api = WHOISApi(ApiClient(Configuration()))
resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)
```

Run it:

```bash
python main.py
```

## Configure

See [Authentication](../authentication.md) for how to obtain a key. Minimal setup:

```python
"""Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

## Endpoints

All 55 endpoints are shown below, grouped by category. Each includes its method, path, parameters, and a runnable example. See the [full endpoint reference](../endpoints/README.md) for response shapes and field details.

### WHOIS

#### Live WHOIS Lookup

`GET /v2.0/whois/live`

```python
"""Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

#### WHOIS Historical or Reverse Lookup

`GET /v1.0/whois`

```python
"""Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

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
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_historical_or_reverse_with_http_info(api_key="YOUR_API_KEY", whois="historical", domain_name="example.com", exact=True)
print("status:", resp.status_code)
print(resp.data)

```

#### Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

```python
"""Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest

# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
config = Configuration()
api = WHOISApi(ApiClient(config))

bulk_whois_request = BulkWhoisRequest()  # populate fields as needed
resp = api.bulk_whois_with_http_info(api_key="YOUR_API_KEY", bulk_whois_request=bulk_whois_request)
print("status:", resp.status_code)
print(resp.data)

```

#### Historical WHOIS records for a domain

`GET /v2.0/whois/history`

```python
"""Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_history_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

#### Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

```python
"""Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_reverse_with_http_info(api_key="YOUR_API_KEY", keyword="value")
print("status:", resp.status_code)
print(resp.data)

```

### DNS

#### Live DNS Lookup

`GET /v2.0/dns/live`

```python
"""Runnable example: Live DNS Lookup (GET /v2.0/dns/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsLive (GET /v2.0/dns/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", ip_address="8.8.8.8", var_type="value")
print("status:", resp.status_code)
print(resp.data)

```

#### Historical DNS Lookup

`GET /v2.0/dns/historical`

```python
"""Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_historical_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", var_type="value")
print("status:", resp.status_code)
print(resp.data)

```

#### Reverse DNS Lookup

`GET /v2.1/dns/reverse`

```python
"""Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_reverse_with_http_info(api_key="YOUR_API_KEY", value="value", var_type="a", exact=True)
print("status:", resp.status_code)
print(resp.data)

```

#### Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

```python
"""Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest

# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
config = Configuration()
api = DNSApi(ApiClient(config))

dns_bulk_request = DnsBulkRequest()  # populate fields as needed
resp = api.dns_bulk_with_http_info(api_key="YOUR_API_KEY", var_type="value", dns_bulk_request=dns_bulk_request)
print("status:", resp.status_code)
print(resp.data)

```

### Domain Availability

#### Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

```python
"""Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi

# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainAvailabilityApi(ApiClient(config))

resp = api.domain_availability_v2_with_http_info(api_key="YOUR_API_KEY", domain="example.com")
print("status:", resp.status_code)
print(resp.data)

```

#### Bulk Domain Availability Check

`POST /v2.0/domain/availability`

```python
"""Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi
from whoisfreaks.models.bulk_domain_availability_request import BulkDomainAvailabilityRequest

# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
config = Configuration()
api = DomainAvailabilityApi(ApiClient(config))

bulk_domain_availability_request = BulkDomainAvailabilityRequest()  # populate fields as needed
resp = api.bulk_domain_availability_v2_with_http_info(api_key="YOUR_API_KEY", bulk_domain_availability_request=bulk_domain_availability_request)
print("status:", resp.status_code)
print(resp.data)

```

### Typosquatting

#### Typosquatting Lookup

`GET /v3.0/domain/typos`

```python
"""Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.typosquatting_api import TyposquattingApi

# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
config = Configuration()
api = TyposquattingApi(ApiClient(config))

resp = api.typosquatting_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

### SSL

#### SSL Certificate Lookup

`GET /v1.0/ssl/live`

```python
"""Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ssl_api import SSLApi

# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = SSLApi(ApiClient(config))

resp = api.ssl_lookup_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

### Geolocation

#### IP Geolocation Lookup

`GET /v1.0/geolocation`

```python
"""Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi

# Parameters for geolocation (GET /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
config = Configuration()
api = GeolocationApi(ApiClient(config))

resp = api.geolocation_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)

```

#### Bulk IP Geolocation

`POST /v1.0/geolocation`

```python
"""Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
api = GeolocationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
resp = api.bulk_geolocation_with_http_info(api_key="YOUR_API_KEY", bulk_geolocation_request=bulk_geolocation_request)
print("status:", resp.status_code)
print(resp.data)

```

### Subdomains

#### Subdomains Lookup

`GET /v1.0/subdomains`

```python
"""Runnable example: Subdomains Lookup (GET /v1.0/subdomains)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.subdomains_api import SubdomainsApi

# Parameters for subdomains (GET /v1.0/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = SubdomainsApi(ApiClient(config))

resp = api.subdomains_with_http_info(api_key="YOUR_API_KEY", domain="example.com", after="2000-01-01", before=str(date.today()))
print("status:", resp.status_code)
print(resp.data)

```

### IP Reputation

#### IP Reputation Lookup

`GET /v1.0/security`

```python
"""Runnable example: IP Reputation Lookup (GET /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi

# Parameters for ipReputation (GET /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
config = Configuration()
api = IPReputationApi(ApiClient(config))

resp = api.ip_reputation_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)

```

#### Bulk IP Reputation

`POST /v1.0/security`

```python
"""Runnable example: Bulk IP Reputation (POST /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkIpReputation (POST /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
api = IPReputationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
resp = api.bulk_ip_reputation_with_http_info(api_key="YOUR_API_KEY", bulk_geolocation_request=bulk_geolocation_request)
print("status:", resp.status_code)
print(resp.data)

```

### Domain Reputation

#### Domain Reputation Lookup

`GET /v1/domain/security`

```python
"""Runnable example: Domain Reputation Lookup (GET /v1/domain/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_reputation_api import DomainReputationApi

# Parameters for domainReputation (GET /v1/domain/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainReputationApi(ApiClient(config))

resp = api.domain_reputation_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

### ASN WHOIS

#### ASN WHOIS Lookup

`GET /v2.0/asn-whois`

```python
"""Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.asnwhois_api import ASNWHOISApi

# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = ASNWHOISApi(ApiClient(config))

resp = api.asn_whois_with_http_info(api_key="YOUR_API_KEY", asn="AS15169")
print("status:", resp.status_code)
print(resp.data)

```

### IP WHOIS

#### IP WHOIS Lookup

`GET /v1.0/ip-whois`

```python
"""Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ipwhois_api import IPWHOISApi

# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = IPWHOISApi(ApiClient(config))

resp = api.ip_whois_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)

```

### Account

#### Rotate API Key

`GET /v1.0/api-key/rotate`

```python
"""Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.rotate_api_key_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

#### Account Usage

`GET /v1.0/whoisapi/usage`

```python
"""Runnable example: Account Usage (GET /v1.0/whoisapi/usage)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.account_usage_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

#### Database File Status (Public)

`GET /v3.3/status`

```python
"""Runnable example: Database File Status (Public) (GET /v3.3/status)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for databaseFileStatus (GET /v3.3/status):
#   (no parameters besides apiKey)
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.database_file_status_with_http_info()
print("status:", resp.status_code)
print(resp.data)

```

### Databases - Newly Registered

#### Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

```python
"""Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtld.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtld.gz")

```

#### Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

```python
"""Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_cctld(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyCctld.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyCctld.gz")

```

#### Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

```python
"""Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld_cleaned(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtldCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtldCleaned.gz")

```

#### Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

```python
"""Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_cctld_cleaned(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyCctldCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyCctldCleaned.gz")

```

#### Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

```python
"""Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

resp = api.db_newly_gtld_json_with_http_info(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))
print("status:", resp.status_code)
print(resp.data)

```

#### Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

```python
"""Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

resp = api.db_newly_cctld_json_with_http_info(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))
print("status:", resp.status_code)
print(resp.data)

```

#### Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

```python
"""Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_dns(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyDns.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyDns.gz")

```

### Databases - Expiring & Dropped

#### Expiring Domains

`GET /v3.1/download/domainer/expired`

```python
"""Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_expired(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbExpired.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbExpired.gz")

```

#### Expiring Cleaned WHOIS

`GET /v3.1/download/domainer/expired/cleaned`

```python
"""Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_expired_cleaned(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbExpiredCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbExpiredCleaned.gz")

```

#### Dropped Domains

`GET /v3.1/download/domainer/dropped`

```python
"""Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_dropped(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDropped.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDropped.gz")

```

#### Dropped Domains (JSON)

`GET /v3.1/domains/dropped`

```python
"""Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

resp = api.db_dropped_json_with_http_info(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))
print("status:", resp.status_code)
print(resp.data)

```

#### Dropped With Backlinks

`GET /v3.3/download/domainer/dropped/backlinks`

```python
"""Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_expiring_dropped_api import DatabasesExpiringDroppedApi

# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesExpiringDroppedApi(ApiClient(config))

data = api.db_dropped_backlinks(api_key="YOUR_API_KEY", whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDroppedBacklinks.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDroppedBacklinks.gz")

```

### Databases - WHOIS

#### WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

```python
"""Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_daily(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisDaily.gz")

```

#### WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

```python
"""Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisWeekly.gz")

```

#### WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

```python
"""Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_monthly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisMonthly.gz")

```

### Databases - DNS

#### DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

```python
"""Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_daily(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsDaily.gz")

```

#### DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

```python
"""Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsWeekly.gz")

```

#### DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

```python
"""Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_monthly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsMonthly.gz")

```

### Databases - Subdomains

#### Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

```python
"""Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_daily(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsDaily.gz")

```

#### Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

```python
"""Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsWeekly.gz")

```

#### Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

```python
"""Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_monthly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsMonthly.gz")

```

### Databases - IP Geolocation

#### IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

```python
"""Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

resp = api.db_ip_country_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

#### IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

```python
"""Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_country(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCountry.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCountry.gz")

```

#### IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

```python
"""Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

resp = api.db_ip_city_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

#### IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

```python
"""Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_city(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCity.gz")

```

### Databases - ASN WHOIS

#### ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

```python
"""Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

data = api.db_asn_whois(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbAsnWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbAsnWhois.gz")

```

#### ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

```python
"""Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

resp = api.db_asn_whois_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

### Databases - IP WHOIS

#### IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

```python
"""Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPWHOISApi(ApiClient(config))

data = api.db_ip_whois(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpWhois.gz")

```

#### IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

```python
"""Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPWHOISApi(ApiClient(config))

resp = api.db_ip_whois_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

### Databases - IP Security

#### IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

```python
"""Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPSecurityApi(ApiClient(config))

data = api.db_ip_security(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpSecurity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpSecurity.gz")

```

#### IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

```python
"""Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPSecurityApi(ApiClient(config))

resp = api.db_ip_security_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```
