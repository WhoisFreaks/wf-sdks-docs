# Endpoint Reference

The WhoisFreaks API exposes **53 endpoints** across **21 categories**. Every endpoint is available in all 10 SDKs. Browse by category:

- [WHOIS](whois.md) — 3 endpoint(s)
- [DNS](dns.md) — 4 endpoint(s)
- [Domain Availability](domain-availability.md) — 2 endpoint(s)
- [Typosquatting](typosquatting.md) — 1 endpoint(s)
- [SSL](ssl.md) — 1 endpoint(s)
- [Geolocation](geolocation.md) — 2 endpoint(s)
- [Subdomains](subdomains.md) — 1 endpoint(s)
- [IP Reputation](ip-reputation.md) — 2 endpoint(s)
- [Domain Reputation](domain-reputation.md) — 1 endpoint(s)
- [ASN WHOIS](asn-whois.md) — 1 endpoint(s)
- [IP WHOIS](ip-whois.md) — 1 endpoint(s)
- [Account](account.md) — 3 endpoint(s)
- [Databases - Newly Registered](databases-newly-registered.md) — 7 endpoint(s)
- [Databases - Expiring & Dropped](databases-expiring-dropped.md) — 5 endpoint(s)
- [Databases - WHOIS](databases-whois.md) — 3 endpoint(s)
- [Databases - DNS](databases-dns.md) — 3 endpoint(s)
- [Databases - Subdomains](databases-subdomains.md) — 3 endpoint(s)
- [Databases - IP Geolocation](databases-ip-geolocation.md) — 4 endpoint(s)
- [Databases - ASN WHOIS](databases-asn-whois.md) — 2 endpoint(s)
- [Databases - IP WHOIS](databases-ip-whois.md) — 2 endpoint(s)
- [Databases - IP Security](databases-ip-security.md) — 2 endpoint(s)

## Full endpoint list

| Category | Method | Path | Operation |
|----------|--------|------|-----------|
| WHOIS | GET | `/v2.0/whois/live` | `whoisLive` |
| WHOIS | GET | `/v1.0/whois` | `whoisHistoricalOrReverse` |
| WHOIS | POST | `/v2.0/bulkwhois/live` | `bulkWhois` |
| DNS | GET | `/v2.0/dns/live` | `dnsLive` |
| DNS | GET | `/v2.0/dns/historical` | `dnsHistorical` |
| DNS | GET | `/v2.1/dns/reverse` | `dnsReverse` |
| DNS | POST | `/v2.0/dns/bulk/live` | `dnsBulk` |
| Domain Availability | GET | `/v2.0/domain/availability` | `domainAvailabilityV2` |
| Domain Availability | POST | `/v2.0/domain/availability` | `bulkDomainAvailabilityV2` |
| Typosquatting | GET | `/v3.0/domain/typos` | `typosquatting` |
| SSL | GET | `/v1.0/ssl/live` | `sslLookup` |
| Geolocation | GET | `/v1.0/geolocation` | `geolocation` |
| Geolocation | POST | `/v1.0/geolocation` | `bulkGeolocation` |
| Subdomains | GET | `/v1.0/subdomains` | `subdomains` |
| IP Reputation | GET | `/v1.0/security` | `ipReputation` |
| IP Reputation | POST | `/v1.0/security` | `bulkIpReputation` |
| Domain Reputation | GET | `/v1/domain/security` | `domainReputation` |
| ASN WHOIS | GET | `/v2.0/asn-whois` | `asnWhois` |
| IP WHOIS | GET | `/v1.0/ip-whois` | `ipWhois` |
| Account | GET | `/v1.0/api-key/rotate` | `rotateApiKey` |
| Account | GET | `/v1.0/whoisapi/usage` | `accountUsage` |
| Account | GET | `/v3.3/status` | `databaseFileStatus` |
| Databases - Newly Registered | GET | `/v3.1/download/domainer/gtld` | `dbNewlyGtld` |
| Databases - Newly Registered | GET | `/v3.1/download/domainer/cctld` | `dbNewlyCctld` |
| Databases - Newly Registered | GET | `/v3.1/download/domainer/gtld/cleaned` | `dbNewlyGtldCleaned` |
| Databases - Newly Registered | GET | `/v3.1/download/domainer/cctld/cleaned` | `dbNewlyCctldCleaned` |
| Databases - Newly Registered | GET | `/v3.1/domains/newly/gtld` | `dbNewlyGtldJson` |
| Databases - Newly Registered | GET | `/v3.1/domains/newly/cctld` | `dbNewlyCctldJson` |
| Databases - Newly Registered | GET | `/v3.1/download/domainer/newly/dns` | `dbNewlyDns` |
| Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/expired` | `dbExpired` |
| Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/expired/cleaned` | `dbExpiredCleaned` |
| Databases - Expiring & Dropped | GET | `/v3.1/download/domainer/dropped` | `dbDropped` |
| Databases - Expiring & Dropped | GET | `/v3.1/domains/dropped` | `dbDroppedJson` |
| Databases - Expiring & Dropped | GET | `/v3.3/download/domainer/dropped/backlinks` | `dbDroppedBacklinks` |
| Databases - WHOIS | GET | `/v3.3/download/dbupdate/daily/domains/whois` | `dbWhoisDaily` |
| Databases - WHOIS | GET | `/v3.3/download/dbupdate/weekly/domains/whois` | `dbWhoisWeekly` |
| Databases - WHOIS | GET | `/v3.3/download/dbupdate/monthly/domains/whois` | `dbWhoisMonthly` |
| Databases - DNS | GET | `/v3.2/download/dbupdate/daily/dns` | `dbDnsDaily` |
| Databases - DNS | GET | `/v3.2/download/dbupdate/weekly/dns` | `dbDnsWeekly` |
| Databases - DNS | GET | `/v3.2/download/dbupdate/monthly/dns` | `dbDnsMonthly` |
| Databases - Subdomains | GET | `/v3.2/download/dbupdate/daily/subdomains` | `dbSubdomainsDaily` |
| Databases - Subdomains | GET | `/v3.2/download/dbupdate/weekly/subdomains` | `dbSubdomainsWeekly` |
| Databases - Subdomains | GET | `/v3.2/download/dbupdate/monthly/subdomains` | `dbSubdomainsMonthly` |
| Databases - IP Geolocation | GET | `/v3.3/status/snapshot/ip/country` | `dbIpCountryStatus` |
| Databases - IP Geolocation | GET | `/v3.3/download/snapshot/ip/country` | `dbIpCountry` |
| Databases - IP Geolocation | GET | `/v3.3/status/snapshot/ip/city` | `dbIpCityStatus` |
| Databases - IP Geolocation | GET | `/v3.3/download/snapshot/ip/city` | `dbIpCity` |
| Databases - ASN WHOIS | GET | `/v3.3/download/snapshot/asn/whois` | `dbAsnWhois` |
| Databases - ASN WHOIS | GET | `/v3.3/status/snapshot/asn/whois` | `dbAsnWhoisStatus` |
| Databases - IP WHOIS | GET | `/v3.3/download/snapshot/ip/whois` | `dbIpWhois` |
| Databases - IP WHOIS | GET | `/v3.3/status/snapshot/ip/whois` | `dbIpWhoisStatus` |
| Databases - IP Security | GET | `/v3.3/download/snapshot/ip/security` | `dbIpSecurity` |
| Databases - IP Security | GET | `/v3.3/status/snapshot/ip/security` | `dbIpSecurityStatus` |
