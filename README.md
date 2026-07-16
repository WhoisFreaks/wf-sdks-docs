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

| Language | Registry | Package | Guide |
|----------|----------|---------|-------|
| Python | PyPI | `whoisfreaks` | [Guide](docs/languages/python.md) |
| JavaScript | npm | `whoisfreaks-js` | [Guide](docs/languages/javascript.md) |
| TypeScript | npm | `whoisfreaks` | [Guide](docs/languages/typescript.md) |
| Java | Maven Central | `com.whoisfreaks:whoisfreaks` | [Guide](docs/languages/java.md) |
| Kotlin | Maven Central | `com.whoisfreaks:whoisfreaks` | [Guide](docs/languages/kotlin.md) |
| C# / .NET | NuGet | `WhoisFreaks` | [Guide](docs/languages/csharp.md) |
| Ruby | RubyGems | `whoisfreaks` | [Guide](docs/languages/ruby.md) |
| Go | Go modules | `github.com/WhoisFreaks/whoisfreaks-go` | [Guide](docs/languages/go.md) |
| Swift | Swift PM | `github.com/WhoisFreaks/whoisfreaks-swift` | [Guide](docs/languages/swift.md) |
| PHP | Packagist | `WhoisFreaks/whoisfreaks-php` | [Guide](docs/languages/php.md) |

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

## Endpoint categories

| Category | Endpoints |
|----------|-----------|
| [WHOIS](docs/endpoints/whois.md) | 4 |
| [DNS](docs/endpoints/dns.md) | 4 |
| [Domain Availability](docs/endpoints/domain-availability.md) | 2 |
| [Typosquatting](docs/endpoints/typosquatting.md) | 1 |
| [SSL](docs/endpoints/ssl.md) | 1 |
| [Geolocation](docs/endpoints/geolocation.md) | 2 |
| [Subdomains](docs/endpoints/subdomains.md) | 1 |
| [IP Reputation](docs/endpoints/ip-reputation.md) | 2 |
| [Domain Reputation](docs/endpoints/domain-reputation.md) | 1 |
| [ASN WHOIS](docs/endpoints/asn-whois.md) | 1 |
| [IP WHOIS](docs/endpoints/ip-whois.md) | 1 |
| [Account](docs/endpoints/account.md) | 3 |
| [Databases - Newly Registered](docs/endpoints/databases-newly-registered.md) | 7 |
| [Databases - Expiring & Dropped](docs/endpoints/databases-expiring-dropped.md) | 5 |
| [Databases - WHOIS](docs/endpoints/databases-whois.md) | 3 |
| [Databases - DNS](docs/endpoints/databases-dns.md) | 3 |
| [Databases - Subdomains](docs/endpoints/databases-subdomains.md) | 3 |
| [Databases - IP Geolocation](docs/endpoints/databases-ip-geolocation.md) | 4 |
| [Databases - ASN WHOIS](docs/endpoints/databases-asn-whois.md) | 2 |
| [Databases - IP WHOIS](docs/endpoints/databases-ip-whois.md) | 2 |
| [Databases - IP Security](docs/endpoints/databases-ip-security.md) | 2 |

See the [full endpoint reference](docs/endpoints/README.md) for the complete
list with parameters and per-language examples.

## Authentication at a glance

All requests require an `apiKey` query parameter. Get a key at
<https://billing.whoisfreaks.com>, then configure it once via each SDK's
configuration object — see [Authentication](docs/authentication.md).

Base URLs:

| Purpose | URL |
|---------|-----|
| Live lookups | `https://api.whoisfreaks.com` |
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
