# WhoisFreaks SDK Documentation

Official documentation for the **WhoisFreaks** SDKs — one API, 10
languages, 54 endpoints. Every SDK is generated from the same
[OpenAPI specification](https://whoisfreaks.com/documentation) and published to
its language's standard registry.

> Complete WhoisFreaks API — WHOIS, DNS, SSL, Geolocation, Typosquatting, IP Intelligence, Domain Reputation, and bulk database downloads.

## Contents

- [Authentication](docs/authentication.md) — get and configure your API key
- [Language guides](#language-guides) — install + usage for each SDK
- [Endpoint reference](docs/endpoints/README.md) — all 54 endpoints, grouped by category
- [Runnable examples](examples/README.md) — copy-paste, ready-to-run example for every endpoint in every language

## Language guides

| Language   | Registry      | Package                                    | Guide                                 |
| ---------- | ------------- | ------------------------------------------ | ------------------------------------- |
| Python     | PyPI          | `whoisfreaks`                              | [Guide](docs/languages/python.md)     |
| JavaScript | npm           | `whoisfreaks-js`                           | [Guide](docs/languages/javascript.md) |
| TypeScript | npm           | `whoisfreaks`                              | [Guide](docs/languages/typescript.md) |
| Java       | Maven Central | `com.whoisfreaks:whoisfreaks`              | [Guide](docs/languages/java.md)       |
| Kotlin     | Maven Central | `com.whoisfreaks:whoisfreaks`              | [Guide](docs/languages/kotlin.md)     |
| C# / .NET  | NuGet         | `WhoisFreaks`                              | [Guide](docs/languages/csharp.md)     |
| Ruby       | RubyGems      | `whoisfreaks`                              | [Guide](docs/languages/ruby.md)       |
| Go         | Go modules    | `github.com/WhoisFreaks/whoisfreaks-go`    | [Guide](docs/languages/go.md)         |
| Swift      | Swift PM      | `github.com/WhoisFreaks/whoisfreaks-swift` | [Guide](docs/languages/swift.md)      |
| PHP        | Packagist     | `WhoisFreaks/whoisfreaks-php`              | [Guide](docs/languages/php.md)        |

## Quick start

Pick your language, install the package, set your API key, and call an endpoint.
Example (Python):

```bash
pip install whoisfreaks
```

```python
import whoisfreaks
from whoisfreaks import Configuration, ApiClient

config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"
client = ApiClient(config)

result = client.whois_live(domainName="example.com")
print(result)
```

The equivalent for every other language is in its [language guide](#language-guides).

## Endpoint sections

The API is organized into three sections. See the [full endpoint reference](docs/endpoints/README.md) for every operation with parameters, response fields, and per-language examples.

### [API Solutions](docs/endpoints/api-solutions.md) — 20 endpoints

Real-time and on-demand lookup APIs. Query a single domain, IP, or ASN and get structured JSON (or XML) back immediately.

[WHOIS](docs/endpoints/whois.md), [DNS](docs/endpoints/dns.md), [Domain Availability](docs/endpoints/domain-availability.md), [Typosquatting](docs/endpoints/typosquatting.md), [SSL](docs/endpoints/ssl.md), [Geolocation](docs/endpoints/geolocation.md), [Subdomains](docs/endpoints/subdomains.md), [IP Reputation](docs/endpoints/ip-reputation.md), [Domain Reputation](docs/endpoints/domain-reputation.md), [ASN WHOIS](docs/endpoints/asn-whois.md), [IP WHOIS](docs/endpoints/ip-whois.md)

### [Databases](docs/endpoints/databases.md) — 31 endpoints

Bulk data feeds and downloadable database snapshots for large-scale processing — newly registered, expiring/dropped, and full WHOIS/DNS/IP datasets.

[Databases - Newly Registered](docs/endpoints/databases-newly-registered.md), [Databases - Expiring & Dropped](docs/endpoints/databases-expiring-dropped.md), [Databases - WHOIS](docs/endpoints/databases-whois.md), [Databases - DNS](docs/endpoints/databases-dns.md), [Databases - Subdomains](docs/endpoints/databases-subdomains.md), [Databases - IP Geolocation](docs/endpoints/databases-ip-geolocation.md), [Databases - ASN WHOIS](docs/endpoints/databases-asn-whois.md), [Databases - IP WHOIS](docs/endpoints/databases-ip-whois.md), [Databases - IP Security](docs/endpoints/databases-ip-security.md)

### [Account & Utilities](docs/endpoints/account-utilities.md) — 3 endpoints

Manage your account, monitor API usage and credits, and rotate your API key.

[Account](docs/endpoints/account.md)

## Authentication at a glance

All requests require an `apiKey` query parameter. Get a key at
<https://billing.whoisfreaks.com>, then configure it once via each SDK's
configuration object — see [Authentication](docs/authentication.md).

Base URLs:

| Purpose            | URL                             |
| ------------------ | ------------------------------- |
| APIs               | `https://api.whoisfreaks.com`   |
| Database downloads | `https://files.whoisfreaks.com` |

## About these docs

These docs are generated from the OpenAPI spec by `scripts/gen_docs.py`, so they
stay in sync with the API. To regenerate after a spec change:

```bash
python3 scripts/gen_docs.py path/to/whoisfreaks-openapi.yaml .
```

## Support

- API docs: <https://whoisfreaks.com/documentation>
- Billing & keys: <https://billing.whoisfreaks.com>
- Email: support@whoisfreaks.com

## License

MIT — see individual SDK repositories for details.
