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

All 53 endpoints are available. A few common examples follow; see the [full endpoint reference](../endpoints/README.md) for every operation, its parameters, and response shape.

### WHOIS: Live WHOIS Lookup

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

### DNS: Live DNS Lookup

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

### Domain Availability: Domain Availability Check with Suggestions

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

### Typosquatting: Typosquatting Lookup

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

### SSL: SSL Certificate Lookup

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

### Geolocation: IP Geolocation Lookup

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

### Subdomains: Subdomains Lookup

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

### IP Reputation: IP Reputation Lookup

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

### Domain Reputation: Domain Reputation Lookup

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

### ASN WHOIS: ASN WHOIS Lookup

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

### IP WHOIS: IP WHOIS Lookup

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

### Account: Rotate API Key

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

### Databases - Newly Registered: Newly Registered gTLD (CSV)

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

### Databases - Expiring & Dropped: Expiring Domains

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

### Databases - WHOIS: WHOIS Database Daily

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

### Databases - DNS: DNS Database Daily

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

### Databases - Subdomains: Subdomains Daily

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

### Databases - IP Geolocation: IP to Country Snapshot Status

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

### Databases - ASN WHOIS: ASN WHOIS Snapshot

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

### Databases - IP WHOIS: IP WHOIS Snapshot

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

### Databases - IP Security: IP Security Snapshot

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
