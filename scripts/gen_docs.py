#!/usr/bin/env python3
"""Generate the WhoisFreaks SDK documentation monorepo from the OpenAPI spec.

Docs-as-code: every endpoint reference, parameter table, and per-language usage
example is derived from spec/whoisfreaks-openapi.yaml, so the docs stay accurate
and can be regenerated whenever the spec changes.

Output tree (under OUT_DIR):
  README.md                      root doc (install + quickstart for all languages)
  docs/authentication.md         API key setup, shared by all SDKs
  docs/languages/<lang>.md        install + configure + full endpoint usage per language
  docs/endpoints/README.md        endpoint catalog (grouped by tag)
  docs/endpoints/<slug>.md        per-tag reference: each operation, params, examples
"""
import os, re, sys, yaml, pathlib

SPEC = sys.argv[1] if len(sys.argv) > 1 else "spec/whoisfreaks-openapi.yaml"
OUT  = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "docs-repo")
OWNER = os.environ.get("OWNER", "whoisfreaks")

spec = yaml.safe_load(open(SPEC))
comps = spec.get("components", {})

def deref(node):
    if isinstance(node, dict) and "$ref" in node:
        _, _, section, name = node["$ref"].split("/")
        return comps.get(section, {}).get(name, {})
    return node

# ---- registry / install metadata per language -------------------------------
# name  = install identifier on the registry
# repo  = git distribution repo (for git-based langs)
LANGS = {
    "python":     {"label": "Python",     "registry": "PyPI",          "pkg": "whoisfreaks"},
    "javascript": {"label": "JavaScript", "registry": "npm",           "pkg": "whoisfreaks-js"},
    "typescript": {"label": "TypeScript", "registry": "npm",           "pkg": "whoisfreaks"},
    "java":       {"label": "Java",       "registry": "Maven Central",  "pkg": "com.whoisfreaks:whoisfreaks"},
    "kotlin":     {"label": "Kotlin",     "registry": "Maven Central",  "pkg": "com.whoisfreaks:whoisfreaks"},
    "csharp":     {"label": "C# / .NET",  "registry": "NuGet",          "pkg": "WhoisFreaks"},
    "ruby":       {"label": "Ruby",       "registry": "RubyGems",       "pkg": "whoisfreaks"},
    "go":         {"label": "Go",         "registry": "Go modules",     "pkg": f"github.com/{OWNER}/whoisfreaks-go"},
    "swift":      {"label": "Swift",      "registry": "Swift PM",       "pkg": f"github.com/{OWNER}/whoisfreaks-swift"},
    "php":        {"label": "PHP",        "registry": "Packagist",      "pkg": f"{OWNER}/whoisfreaks-php"},
}
LANG_ORDER = list(LANGS.keys())

def install_snippet(lang, version="LATEST"):
    m = LANGS[lang]; pkg = m["pkg"]
    if lang == "python":
        return "bash", f"pip install {pkg}"
    if lang == "javascript":
        return "bash", f"npm install {pkg}"
    if lang == "typescript":
        return "bash", f"npm install {pkg}"
    if lang == "java":
        g, a = pkg.split(":")
        return "xml", (f"<dependency>\n  <groupId>{g}</groupId>\n"
                       f"  <artifactId>{a}</artifactId>\n  <version>{version}</version>\n</dependency>")
    if lang == "kotlin":
        return "kotlin", f'implementation("{pkg}:{version}")'
    if lang == "csharp":
        return "bash", f"dotnet add package {pkg}"
    if lang == "ruby":
        return "bash", f"gem install {pkg}"
    if lang == "go":
        return "bash", f"go get {pkg}"
    if lang == "swift":
        return "swift", (f'.package(url: "https://{pkg}.git", from: "{version}")')
    if lang == "php":
        return "bash", f"composer require {pkg}"
    return "bash", ""

# ---- per-language "create a new project" walkthrough ------------------------
def getting_started(lang):
    """Full copy-paste steps: make a fresh project, add the SDK, and run.
    Written so someone with only the language's toolchain installed can go
    from empty directory to a running program."""
    m = LANGS[lang]; pkg = m["pkg"]
    S = []  # list of (markdown) lines

    if lang == "python":
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "python3 -m venv .venv",
            "source .venv/bin/activate        # Windows: .venv\\Scripts\\activate",
            f"pip install {pkg}",
            "```",
            "",
            "Create `main.py`:", "",
            "```python",
            "from whoisfreaks import Configuration, ApiClient",
            "from whoisfreaks.api.whois_api import WHOISApi",
            "",
            "api = WHOISApi(ApiClient(Configuration()))",
            'resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")',
            'print("status:", resp.status_code)',
            "print(resp.data)",
            "```",
            "",
            "Run it:", "",
            "```bash", "python main.py", "```",
        ]
    elif lang in ("javascript", "typescript"):
        ext = "js" if lang == "javascript" else "ts"
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "npm init -y",
            f"npm install {pkg}",
        ]
        if lang == "typescript":
            S += ["npm install -D typescript ts-node @types/node"]
        S += ["```", ""]
        if lang == "typescript":
            # TS package is ESM
            S += ["Set `\"type\": \"module\"` in `package.json`, then create "
                  f"`main.{ext}`:", "", f"```{ext}",
                  f'import {{ Configuration, WHOISApi }} from "{pkg}";', "",
                  "const api = new WHOISApi(new Configuration());", "",
                  "const resp = await api.whoisLiveRaw({ apiKey: \"YOUR_API_KEY\", domainName: \"example.com\" });",
                  'console.log("status:", resp.raw.status);',
                  "console.log(await resp.value());", "```", "", "Run it:", "",
                  "```bash", f"npx ts-node main.{ext}", "```"]
        else:
            # JS package uses the `javascript` generator: no Configuration class,
            # apiKey passed positionally, methods return Promises.
            S += [f"Create `main.{ext}`:", "", f"```{ext}",
                  "// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)",
                  f'import pkg from "{pkg}";',
                  "const { ApiClient, WHOISApi } = pkg;",
                  f'// or:  const {{ ApiClient, WHOISApi }} = require("{pkg}");', "",
                  "const api = new WHOISApi();   // uses ApiClient.instance", "",
                  'api.whoisLive("YOUR_API_KEY", "example.com")',
                  "  .then(data => console.log(data))",
                  "  .catch(err => console.error(err));", "```", "", "Run it:", "",
                  "```bash", f"node main.{ext}", "```"]
    elif lang == "csharp":
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "dotnet new console",
            f"dotnet add package {pkg}",
            "```",
            "",
            "Replace `Program.cs` with:", "",
            "```csharp",
            "using System;",
            "using WhoisFreaks.Api;",
            "using WhoisFreaks.Client;",
            "",
            "var config = new Configuration { BasePath = \"https://api.whoisfreaks.com\" };",
            "var api = new WHOISApi(config);",
            "",
            'var resp = api.WhoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);',
            'Console.WriteLine($"status: {(int)resp.StatusCode}");',
            "Console.WriteLine(resp.Data);",
            "```",
            "",
            "Run it:", "",
            "```bash", "dotnet run", "```",
        ]
    elif lang == "go":
        mod = pkg  # github.com/<owner>/whoisfreaks-go
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "go mod init whoisfreaks-test          # creates go.mod (required)",
            f"go get {mod}",
            "```",
            "",
            "> **Note:** `go get` only works inside a module. If you see "
            "*'go.mod file not found'*, run `go mod init <name>` first (as above).",
            "",
            "Create `main.go`:", "",
            "```go",
            "package main",
            "",
            "import (",
            "    \"context\"",
            "    \"encoding/json\"",
            "    \"fmt\"",
            f"    wf \"{mod}\"",
            ")",
            "",
            "func main() {",
            "    cfg := wf.NewConfiguration()",
            "    client := wf.NewAPIClient(cfg)",
            "    // apiKey is a builder method on the request",
            "    result, httpRes, err := client.WHOISAPI.WhoisLive(context.Background()).ApiKey(\"YOUR_API_KEY\").DomainName(\"example.com\").Execute()",
            "    if err != nil { panic(err) }",
            "    fmt.Println(\"status:\", httpRes.StatusCode)",
            "    b, _ := json.MarshalIndent(result, \"\", \"  \")",
            "    fmt.Println(string(b))",
            "}",
            "```",
            "",
            "Run it:", "",
            "```bash", "go mod tidy", "go run main.go", "```",
        ]
    elif lang == "java":
        g, a = pkg.split(":")
        S += [
            "Create a Maven project and add the dependency to `pom.xml`:", "",
            "```xml",
            "<dependency>",
            f"  <groupId>{g}</groupId>",
            f"  <artifactId>{a}</artifactId>",
            "  <version>LATEST</version>   <!-- pin to a real version, e.g. 1.0.0 -->",
            "</dependency>",
            "```",
            "",
            "`src/main/java/Main.java`:", "",
            "```java",
            "import com.whoisfreaks.client.ApiClient;",
            "import com.whoisfreaks.client.Configuration;",
            "import com.whoisfreaks.client.api.WhoisApi;",
            "",
            "public class Main {",
            "    public static void main(String[] args) throws Exception {",
            "        ApiClient client = Configuration.getDefaultApiClient();",
            "        client.setBasePath(\"https://api.whoisfreaks.com\");",
            "        WhoisApi api = new WhoisApi(client);",
            "        var resp = api.whoisLiveWithHttpInfo(\"YOUR_API_KEY\", \"example.com\", null);",
            "        System.out.println(\"status: \" + resp.getStatusCode());",
            "        System.out.println(resp.getData());",
            "    }",
            "}",
            "```",
            "",
            "Build and run with `mvn compile exec:java -Dexec.mainClass=Main` "
            "(or your IDE).",
        ]
    elif lang == "kotlin":
        S += [
            "In a Gradle project, add to `build.gradle.kts`:", "",
            "```kotlin",
            "repositories { mavenCentral() }",
            "dependencies {",
            f'    implementation("{pkg}:LATEST")   // pin to a real version, e.g. 1.0.0',
            "}",
            "```",
            "",
            "`src/main/kotlin/Main.kt`:", "",
            "```kotlin",
            "import com.whoisfreaks.api.WhoisApi",
            "",
            "fun main() {",
            "    val api = WhoisApi(basePath = \"https://api.whoisfreaks.com\")",
            "    val result = api.whoisLive(\"YOUR_API_KEY\", \"example.com\", null)",
            "    println(result)",
            "}",
            "```",
            "",
            "Run with `./gradlew run` (with the application plugin) or your IDE.",
        ]
    elif lang == "ruby":
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            f"gem install {pkg}",
            "```",
            "",
            "Create `main.rb`:", "",
            "```ruby",
            "require 'whoisfreaks'",
            "",
            "api = WhoisFreaks::WhoisApi.new",
            "data, status, _headers = api.whois_live_with_http_info(api_key: \"YOUR_API_KEY\", domain_name: \"example.com\")",
            "puts \"status: #{status}\"",
            "puts data",
            "```",
            "",
            "Run it:", "",
            "```bash", "ruby main.rb", "```",
        ]
    elif lang == "php":
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "composer init --no-interaction",
            f"composer require {pkg}",
            "```",
            "",
            "Create `main.php`:", "",
            "```php",
            "<?php",
            "require 'vendor/autoload.php';",
            "",
            "$config = WhoisFreaks\\Configuration::getDefaultConfiguration();",
            "$api = new WhoisFreaks\\Api\\WhoisApi(new GuzzleHttp\\Client(), $config);",
            "list($data, $status, $headers) = $api->whoisLiveWithHttpInfo(\"YOUR_API_KEY\", \"example.com\", null);",
            "echo \"status: \" . $status . PHP_EOL;",
            "print_r($data);",
            "```",
            "",
            "Run it:", "",
            "```bash", "php main.php", "```",
        ]
    elif lang == "swift":
        S += [
            "```bash",
            "mkdir whoisfreaks-test && cd whoisfreaks-test",
            "swift package init --type executable",
            "```",
            "",
            "Add the dependency to `Package.swift`:", "",
            "```swift",
            f'.package(url: "https://{pkg}.git", from: "1.0.0"),',
            "```",
            "",
            "…and list `WhoisFreaks` as a target dependency. Then in "
            "`Sources/.../main.swift`:", "",
            "```swift",
            "import WhoisFreaks",
            "",
            "do {",
            "    let result = try await WHOISAPI.whoisLive(apiKey: \"YOUR_API_KEY\", domainName: \"example.com\")",
            "    print(result)",
            "} catch {",
            "    print(error)",
            "}",
            "```",
            "",
            "Run it:", "",
            "```bash", "swift run", "```",
        ]
    return S

# ---- operationId -> per-language method name --------------------------------
def split_words(op_id):
    # camelCase / PascalCase -> words
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1 \2", op_id)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    return [w for w in re.split(r"[\s_]+", s) if w]

def method_name(op_id, lang):
    w = split_words(op_id)
    lower = [x.lower() for x in w]
    if lang in ("python", "ruby"):
        return "_".join(lower)
    # camelCase (lowercase first word): js, ts, php, java, kotlin, swift
    if lang in ("javascript", "typescript", "php", "java", "kotlin", "swift"):
        return lower[0] + "".join(x.capitalize() for x in lower[1:])
    # PascalCase (capitalize first word too): go, csharp
    if lang in ("go", "csharp"):
        return "".join(x.capitalize() for x in lower)
    return op_id

# ---- collect operations, grouped by tag -------------------------------------
import subprocess, glob

def _java_body_models():
    """Authoritative operationId->bodyModel map, read from a generated Java SDK
    if available (sdks/java). The generated code is the source of truth for the
    exact model class name (e.g. bulkDomainAvailabilityV2 -> BulkDomainAvailabilityRequest,
    NOT the spec-derived guess). Falls back to {} if no SDK present."""
    mp = {}
    roots = glob.glob("sdks/java/**/api/*.java", recursive=True)
    pat = re.compile(r"public\s+\S+\s+([a-zA-Z0-9]+)\(String apiKey,\s+([A-Za-z0-9]+Request)\s")
    for fp in roots:
        try:
            txt = open(fp).read()
        except Exception:
            continue
        for mth, model in pat.findall(txt):
            mp[mth] = model
    return mp

_BODY_MAP = _java_body_models()

def _body_model(op):
    rb = op.get("requestBody")
    if not rb:
        return None
    # 1) authoritative: name from generated Java SDK, keyed by operationId
    oid = op.get("operationId") or ""
    if oid in _BODY_MAP:
        return _BODY_MAP[oid]
    # 2) $ref in the spec
    rb = deref(rb)
    sch = ((rb.get("content") or {}).get("application/json") or {}).get("schema") or {}
    if sch.get("$ref"):
        return sch["$ref"].split("/")[-1]
    # 3) last-resort synth (inline body, no generated SDK to consult)
    words = re.sub(r"(.)([A-Z][a-z]+)", r"\1 \2", oid)
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", words)
    return "".join(w.capitalize() for w in re.split(r"[\s_]+", words) if w) + "Request"

def collect():
    out = {}
    for path, item in spec["paths"].items():
        for method, op in item.items():
            if method not in ("get", "post", "put", "delete", "patch"):
                continue
            tag = (op.get("tags") or ["General"])[0]
            params = []
            for pa in op.get("parameters", []):
                pa = deref(pa)
                sc = pa.get("schema", {})
                params.append({
                    "name": pa.get("name"),
                    "in": pa.get("in"),
                    "required": pa.get("required", False),
                    "type": sc.get("type", "string"),
                    "enum": sc.get("enum"),
                    "default": sc.get("default"),
                    "desc": (pa.get("description") or "").strip(),
                })
            # detect binary/file-download responses (application/octet-stream
            # or format: binary) so examples write bytes to a file, not print()
            _r = (op.get("responses") or {}).get("200") or {}
            _r = deref(_r)
            _content = _r.get("content") or {}
            _is_binary = "application/octet-stream" in _content or any(
                (deref(cv).get("schema") or {}).get("format") == "binary"
                for cv in _content.values()
            )
            out.setdefault(tag, []).append({
                "tag": tag,
                "method": method.upper(),
                "path": path,
                "op_id": op.get("operationId") or "",
                "summary": op.get("summary") or "",
                "description": (op.get("description") or "").strip(),
                "params": params,
                "request_body": bool(op.get("requestBody")),
                "body_model": _body_model(op),
                "is_binary": _is_binary,
            })
    return out

OPS = collect()

def slug(tag):
    return re.sub(r"[^a-z0-9]+", "-", tag.lower()).strip("-")

# ---- example call renderer (per language) -----------------------------------
def api_class(tag, lang):
    """Generated API class/type name for a tag. VERIFIED against all 10 real
    generated SDKs:
      * Java is the ONLY language that title-cases acronyms:
        WhoisApi, SslApi, IpWhoisApi, DatabasesIpWhoisApi
      * Every other language keeps acronyms UPPER:
        - python/js/ts/csharp/kotlin/php/ruby: WHOISApi, SSLApi, IPWHOISApi (+ 'Api')
        - swift:  WHOISAPI, SSLAPI, IPWHOISAPI (+ 'API')
        - go:     WHOISAPIService (accessed on the client as .WHOISAPI)
    """
    words = re.sub(r"[^A-Za-z0-9]+", " ", tag).split()
    if lang == "java":
        core = "".join(w.capitalize() for w in words)      # acronyms title-cased
    else:
        core = "".join(w if w.isupper() else w.capitalize() for w in words)
    if lang == "swift":
        return core + "API"
    if lang == "go":
        return core + "APIService"      # the struct type; accessor is core+"API"
    return core + "Api"

def go_accessor(tag):
    """Field name used to reach a service on the Go APIClient, e.g. client.WHOISAPI."""
    words = re.sub(r"[^A-Za-z0-9]+", " ", tag).split()
    return "".join(w if w.isupper() else w.capitalize() for w in words) + "API"

def py_snake(name):
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    return s.lower()

def py_module(cls):
    """Python api module filename (without .py) for a given generated class name.
    openapi-generator inserts '_' at lower->Upper boundaries and at
    ACRONYM->Word boundaries, then lowercases. Acronym runs with no trailing
    lowercase word stay glued: IPWHOISApi -> ipwhois_api, but
    IPReputationApi -> ip_reputation_api. Verified against the real SDK."""
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", cls)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.lower()

def py_param(name):
    """Python parameter name as the generator emits it. openapi-generator
    prefixes 'var_' when a param collides with a Python builtin/type/keyword
    (e.g. 'date' -> 'var_date'). Used only for call keyword args, NOT for
    module/model names."""
    s = py_snake(name)
    PY_RESERVED = {"date", "datetime", "time", "type", "id", "hash",
                   "input", "list", "dict", "set", "str", "bytes", "object",
                   "class", "def", "from", "import", "global", "property"}
    return "var_" + s if s in PY_RESERVED else s

def param_value(p):
    name = p["name"]
    # date-typed params get distinct sentinels resolved per-language:
    #   date   -> yesterday (runtime)
    #   after  -> 2000-01-01 (fixed lower bound)
    #   before -> today (runtime)
    if name == "after":
        return "__DATE_2000__"
    if name == "before":
        return "__TODAY__"
    if name == "date" or p.get("format") == "date":
        return "__YESTERDAY__"
    if name.lower() == "whois" and p["type"] == "boolean":
        return "false"                      # whois flag defaults to false
    if name.lower() == "exact" and p["type"] == "boolean":
        return "true"                       # exact defaults to true
    if "domain" in name.lower():
        return "example.com"
    if "ip" in name.lower():
        return "8.8.8.8"
    if name.lower() == "asn":
        return "AS15169"
    if p["enum"]:
        return p["enum"][0]
    if p["type"] == "boolean":
        return "false"                      # all other booleans default false
    if p["type"] == "integer":
        return "1"
    return "value"

# yesterday-at-runtime expression + value literal per language ----------------
YESTERDAY_EXPR = {
    "python":     "str(date.today() - timedelta(days=1))",
    "javascript": "new Date(Date.now()-86400000).toISOString().slice(0,10)",
    "typescript": "new Date(Date.now()-86400000).toISOString().slice(0,10)",
    "java":       "java.time.LocalDate.now().minusDays(1).toString()",
    "kotlin":     "java.time.LocalDate.now().minusDays(1).toString()",
    "csharp":     "DateTime.UtcNow.AddDays(-1).ToString(\"yyyy-MM-dd\")",
    "ruby":       "(Date.today - 1).to_s",
    "go":         "time.Now().AddDate(0,0,-1).Format(\"2006-01-02\")",
    "php":        "(new DateTime(\"yesterday\"))->format(\"Y-m-d\")",
    "swift":      "String(ISO8601DateFormatter().string(from: Calendar.current.date(byAdding: .day, value: -1, to: Date())!).prefix(10))",
}
TODAY_EXPR = {
    "python":     "str(date.today())",
    "javascript": "new Date().toISOString().slice(0,10)",
    "typescript": "new Date().toISOString().slice(0,10)",
    "java":       "java.time.LocalDate.now().toString()",
    "kotlin":     "java.time.LocalDate.now().toString()",
    "csharp":     "DateTime.UtcNow.ToString(\"yyyy-MM-dd\")",
    "ruby":       "Date.today.to_s",
    "go":         "time.Now().Format(\"2006-01-02\")",
    "php":        "(new DateTime(\"today\"))->format(\"Y-m-d\")",
    "swift":      "String(ISO8601DateFormatter().string(from: Date()).prefix(10))",
}
# fixed lower-bound date for `after`; a plain quoted literal in every language
DATE_2000 = "2000-01-01"
# languages whose date expressions need extra imports / the 'time' package
YESTERDAY_IMPORT = {
    "python": "from datetime import date, timedelta",
    "ruby":   "require 'date'",
    "go":     None,   # 'time' added to import block by the go renderer
}

def _uses_runtime_date(v):
    return v in ("__YESTERDAY__", "__TODAY__")

def lang_literal(lang, value, p):
    """Render a param value as a code literal for the given language.
    Handles date sentinels (yesterday/today/fixed-2000), booleans, strings."""
    is_bool = p.get("type") == "boolean"
    if value == "__YESTERDAY__":
        return YESTERDAY_EXPR.get(lang, '"2000-01-01"'), True
    if value == "__TODAY__":
        return TODAY_EXPR.get(lang, '"2000-01-01"'), True
    if value == "__DATE_2000__":
        return f'"{DATE_2000}"', False      # fixed literal, quoted like a string
    if is_bool:
        truthy = str(value).lower() == "true"
        if lang == "python":
            return ("True" if truthy else "False"), True
        return ("true" if truthy else "false"), True
    return f'"{value}"', False

def ordered_args(op, include_key=True):
    """Ordered (name, value) for the call: required params first (incl apiKey)."""
    out = []
    for p in op["params"]:
        if p["name"] == "apiKey":
            if include_key:
                out.append(("apiKey", "YOUR_API_KEY", p))
            continue
        if p["required"] or p["name"] in ("domainName", "ipAddress", "asn"):
            out.append((p["name"], param_value(p), p))
    return out

COMMENT_PREFIX = {
    "python": "# ", "ruby": "# ", "go": "// ", "php": "// ",
    "javascript": "// ", "typescript": "// ", "java": "// ",
    "kotlin": "// ", "csharp": "// ", "swift": "// ",
}
def params_comment(lang, op):
    """A comment block listing every input parameter: name, type, required/optional,
    and description. Returned as a single string (already comment-prefixed)."""
    pre = COMMENT_PREFIX.get(lang, "# ")
    lines = [f"{pre}Parameters for {op['op_id']} ({op['method']} {op['path']}):"]
    any_p = False
    for p in op["params"]:
        any_p = True
        req = "required" if (p["required"] or p["name"] in ("apiKey","domainName","ipAddress","asn")) else "optional"
        t = p.get("type") or "string"
        if p.get("enum"):
            t += " (one of: " + ", ".join(str(e) for e in p["enum"]) + ")"
        desc = (p.get("desc") or "").strip().replace("\n", " ")
        if len(desc) > 90: desc = desc[:87] + "..."
        line = f"{pre}  - {p['name']} ({t}, {req})"
        if desc: line += f": {desc}"
        lines.append(line)
    if op.get("body_model"):
        lines.append(f"{pre}  - body: {op['body_model']} (required) -- request body object")
    if not any_p and not op.get("body_model"):
        lines.append(f"{pre}  (no parameters besides apiKey)")
    return "\n".join(lines)

def _pascal(op_id):
    return "".join(w.capitalize() for w in split_words(op_id)) or "Example"

def _full_args(op):
    """Every argument in the SDK method's positional order:
       apiKey, required query/path params, requestBody (if any), then optionals.
       Value is None for optional params (rendered as null/None)."""
    required = []
    optional = []
    for p in op["params"]:
        if p["name"] == "apiKey":
            required.append(("apiKey", "YOUR_API_KEY", p)); continue
        if p["required"] or p["name"] in ("domainName", "ipAddress", "asn"):
            required.append((p["name"], param_value(p), p))
        elif p["name"] in ("date", "after", "before") or p.get("format") == "date":
            # date params are commonly the key input for download endpoints;
            # always show them even when technically optional.
            required.append((p["name"], param_value(p), p))
        elif p["name"].lower() in ("whois", "exact") and p["type"] == "boolean":
            # show these flags with their chosen defaults (whois=false, exact=true)
            required.append((p["name"], param_value(p), p))
        else:
            optional.append((p["name"], None, p))
    body = []
    if op.get("body_model"):
        # generator puts the body param right after apiKey & path/query requireds
        bm = op["body_model"]
        bname = bm[0].lower() + bm[1:]  # e.g. BulkWhoisRequest -> bulkWhoisRequest
        body = [("__BODY__:" + bname, bm, {"in": "body", "required": True, "name": bname})]
    return required + body + optional

def _body_ctor(lang, model):
    """A minimal request-body construction line, or (None,None)."""
    if not model: return None
    if lang=="python":      return f"{model}()"
    if lang in ("javascript","typescript"): return "{}"
    if lang=="java":        return f"new {model}()"
    if lang=="kotlin":      return f"{model}()"
    if lang=="csharp":      return f"new {model}()"
    if lang=="ruby":        return f"WhoisFreaks::{model}.new"
    if lang=="go":          return f"*wf.New{model}()"
    if lang=="php":         return f"new WhoisFreaks\\Model\\{model}()"
    if lang=="swift":       return f"{model}()"
    return None

def runnable_example(lang, op):
    m   = method_name(op["op_id"], lang)
    cls = api_class(op["tag"], lang)
    P   = _pascal(op["op_id"])
    args = _full_args(op)                     # ordered (name, value, param)
    bm  = op.get("body_model")

    def is_body(k): return k.startswith("__BODY__:")
    def lit(v, p=None):
        if v is None: return "null"
        if p is not None:
            code, _ = lang_literal(lang, v, p)
            return code
        return f'"{v}"'
    # track whether any date/yesterday expr is used (for imports)
    uses_yesterday = any(v in ("__YESTERDAY__","__TODAY__") for _, v, _ in args)
    pcmt_all = params_comment(lang, op)

    if lang == "python":
        mod = py_module(cls)
        parts=[]; pre=""; needs_date=False
        for k,v,p in args:
            if is_body(k):
                var = py_snake(bm)
                pre = f"{var} = {bm}()  # populate fields as needed\n"
                parts.append(f"{py_snake(k.split(':')[1])}={var}")
            elif v is None:
                continue                       # optional -> omit (has default)
            else:
                lit_v, _isc = lang_literal("python", v, p)
                if v in ("__YESTERDAY__","__TODAY__"): needs_date=True
                parts.append(f"{py_param(k)}={lit_v}")
        date_imp = (YESTERDAY_IMPORT["python"] + "\n") if needs_date else ""
        pcmt = params_comment("python", op) + "\n"
        imp = f"from whoisfreaks.models.{py_snake(bm)} import {bm}\n" if bm else ""
        if op.get("is_binary"):
            fname = (op["op_id"] or "download") + ".gz"
            return (f'"""Runnable example: {op["summary"]} ({op["method"]} {op["path"]}).\n'
                    f'Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""\n'
                    f"{date_imp}from whoisfreaks import Configuration, ApiClient\n"
                    f"from whoisfreaks.api.{mod} import {cls}\n\n"
                    f"{pcmt}"
                    f"config = Configuration()\n"
                    f"api = {cls}(ApiClient(config))\n\n"
                    f"data = api.{m}({', '.join(parts)})   # bytes\n"
                    f'with open("{fname}", "wb") as f:\n'
                    f"    f.write(data)\n"
                    f'print(f"saved {{len(data)}} bytes to {fname}")\n')
        return (f'"""Runnable example: {op["summary"]} ({op["method"]} {op["path"]})."""\n'
                f"{date_imp}from whoisfreaks import Configuration, ApiClient\n"
                f"from whoisfreaks.api.{mod} import {cls}\n{imp}\n"
                f"{pcmt}"
                f"config = Configuration()\n"
                f"api = {cls}(ApiClient(config))\n\n"
                f"{pre}resp = api.{m}_with_http_info({', '.join(parts)})\n"
                f'print("status:", resp.status_code)\n'
                f"print(resp.data)\n")

    if lang in ("javascript","typescript"):
        obj=[]
        for k,v,p in args:
            if is_body(k):
                obj.append(f"{k.split(':')[1]}: {{}}")
            elif v is None:
                obj.append(f"{k}: undefined")
            else:
                cv,_=lang_literal(lang,v,p); obj.append(f'{k}: {cv}')
        objs = ", ".join(obj)
        if lang == "typescript":
            # TS package is ESM: named imports work.
            return (f'// Runnable example: {op["summary"]} ({op["method"]} {op["path"]})\n'
                f"{pcmt_all}\n"
                    f'import {{ Configuration, {cls} }} from "whoisfreaks";\n\n'
                    f'const api = new {cls}(new Configuration());\n\n'
                    f"async function main() {{\n"
                    f"  const resp = await api.{m}Raw({{ {objs} }});\n"
                    f'  console.log("status:", resp.raw.status);\n'
                    f"  console.log(await resp.value());\n"
                    f"}}\nmain().catch(console.error);\n")
        # JavaScript package (whoisfreaks-js) uses the `javascript` generator:
        # no Configuration class; apiKey is passed positionally; methods return
        # Promises. Config/auth lives on ApiClient (ApiClient.instance by default).
        # Build positional args: apiKey, required params, then an opts object for optionals.
        pos = []
        opts = []
        for k, v, p in args:
            if is_body(k):
                pos.append("{}")
            elif v is None:
                cv = "undefined"
                opts.append(f"{k}: undefined")
            else:
                cv, _ = lang_literal("javascript", v, p)
                # first positional args are the required ones (apiKey/domain/etc.)
                if p.get("required") or k in ("apiKey", "domainName", "ipAddress", "asn") \
                   or k in ("date","after","before") or (p.get("type")=="boolean" and k.lower() in ("whois","exact")):
                    pos.append(cv)
                else:
                    opts.append(f"{k}: {cv}")
        pos_str = ", ".join(pos)
        real_opts = [o for o in opts if not o.endswith(": undefined")]
        opts_str = (", { " + ", ".join(real_opts) + " }") if real_opts else ""
        return (f'// Runnable example: {op["summary"]} ({op["method"]} {op["path"]})\n'
                f"{pcmt_all}\n"
                f'// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)\n'
                f'import pkg from "whoisfreaks-js";\n'
                f"const {{ ApiClient, {cls} }} = pkg;\n"
                f'// or:  const {{ ApiClient, {cls} }} = require("whoisfreaks-js");\n\n'
                f"const api = new {cls}();   // uses ApiClient.instance\n\n"
                f"api.{m}({pos_str}{opts_str})\n"
                f"  .then(data => console.log(data))\n"
                f"  .catch(err => console.error(err));\n")

    if lang == "java":
        pos=", ".join(f"new {bm}()" if is_body(k) else lit(v,p) for k,v,p in args)
        imp = f"import com.whoisfreaks.client.model.{bm};\n" if bm else ""
        return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"import com.whoisfreaks.client.ApiClient;\n"
                f"import com.whoisfreaks.client.Configuration;\n"
                f"import com.whoisfreaks.client.api.{cls};\n{imp}\n"
                f"public class {P} {{\n"
                f"    public static void main(String[] args) throws Exception {{\n"
                f"        ApiClient client = Configuration.getDefaultApiClient();\n"
                f'        client.setBasePath("https://api.whoisfreaks.com");\n'
                f"        {cls} api = new {cls}(client);\n"
                f"        var resp = api.{m}WithHttpInfo({pos});\n"
                f'        System.out.println("status: " + resp.getStatusCode());\n'
                f"        System.out.println(resp.getData());\n"
                f"    }}\n}}\n")

    if lang == "kotlin":
        pos=", ".join(f"{bm}()" if is_body(k) else lit(v,p) for k,v,p in args)
        imp = f"import com.whoisfreaks.models.{bm}\n" if bm else ""
        return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"import com.whoisfreaks.api.{cls}\n{imp}\n"
                f"fun main() {{\n"
                f'    val api = {cls}(basePath = "https://api.whoisfreaks.com")\n'
                f"    val result = api.{m}({pos})\n"
                f"    println(result)  // status via api.{m}WithHttpInfo(...).statusCode\n"
                f"}}\n")

    if lang == "csharp":
        pos=", ".join(f"new {bm}()" if is_body(k) else lit(v,p) for k,v,p in args)
        imp = "using WhoisFreaks.Model;\n" if bm else ""
        return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"using System;\nusing WhoisFreaks.Api;\nusing WhoisFreaks.Client;\n{imp}\n"
                f"class {P} {{\n"
                f"    static void Main() {{\n"
                f'        var config = new Configuration {{ BasePath = "https://api.whoisfreaks.com" }};\n'
                f"        var api = new {cls}(config);\n"
                f"        var resp = api.{m}WithHttpInfo({pos});\n"
                f'        Console.WriteLine($"status: {{(int)resp.StatusCode}}");\n'
                f"        Console.WriteLine(resp.Data);\n"
                f"    }}\n}}\n")

    if lang == "ruby":
        pos=[]; opts=[]
        for k,v,p in args:
            if is_body(k):
                pos.append(f"WhoisFreaks::{bm}.new")
            elif v is None:
                continue
            else:
                cv,_=lang_literal('ruby',v,p)
                # required params are positional; optional ones go in the opts hash
                if p.get("required") or k in ("apiKey","domainName","ipAddress","asn") \
                   or k in ("date","after","before") or (p.get("type")=="boolean" and k.lower() in ("whois","exact")):
                    pos.append(cv)
                else:
                    opts.append(f"{py_snake(k)}: {cv}")
        call = ", ".join(pos)
        if opts:
            call += ", { " + ", ".join(opts) + " }"
        return (f"# Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                + ("require 'date'\n" if uses_yesterday else "")
                + f"require 'whoisfreaks'\n\n"
                f"api = WhoisFreaks::{cls}.new\n"
                f"data, status, _headers = api.{m}_with_http_info({call})\n"
                f'puts "status: #{{status}}"\n'
                f"puts data\n")

    if lang == "go":
        builder=""
        for k,v,p in args:
            if k=="apiKey": continue
            if is_body(k):
                builder+=f".{k.split(':')[1][0].upper()+k.split(':')[1][1:]}(*wf.New{bm}())"
            elif v is None:
                continue
            else:
                cv,_=lang_literal("go",v,p); builder+=f'.{k[0].upper()+k[1:]}({cv})'
        _time_imp = '    "time"\n' if uses_yesterday else ''
        call = (f'client.{go_accessor(op["tag"])}.{m}(context.Background())'
                f'.ApiKey("YOUR_API_KEY"){builder}.Execute()')
        if op.get("is_binary"):
            fname = (op["op_id"] or "download") + ".gz"
            return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                    f"{pcmt_all}\n"
                    f"package main\n\n"
                    f'import (\n    "context"\n    "fmt"\n    "os"\n{_time_imp}    wf "github.com/{OWNER}/whoisfreaks-go"\n)\n\n'
                    f"func main() {{\n"
                    f"    cfg := wf.NewConfiguration()\n"
                    f"    client := wf.NewAPIClient(cfg)\n"
                    f"    // returns raw bytes (compressed/binary file) -- write to disk\n"
                    f"    data, _, err := {call}\n"
                    f"    if err != nil {{ panic(err) }}\n"
                    f'    if err := os.WriteFile("{fname}", data, 0644); err != nil {{ panic(err) }}\n'
                    f'    fmt.Printf("saved %d bytes to {fname}\\n", len(data))\n'
                    f"}}\n")
        return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"package main\n\n"
                f'import (\n    "context"\n    "encoding/json"\n    "fmt"\n{_time_imp}    wf "github.com/{OWNER}/whoisfreaks-go"\n)\n\n'
                f"func main() {{\n"
                f"    cfg := wf.NewConfiguration()\n"
                f"    client := wf.NewAPIClient(cfg)\n"
                f"    // apiKey is a builder method on the request, not a config/context value\n"
                f"    result, httpRes, err := {call}\n"
                f"    if err != nil {{ panic(err) }}\n"
                f'    fmt.Println("status:", httpRes.StatusCode)\n'
                f'    b, _ := json.MarshalIndent(result, "", "  ")\n'
                f"    fmt.Println(string(b))\n"
                f"}}\n")

    if lang == "php":
        pos=", ".join(f"new WhoisFreaks\\Model\\{bm}()" if is_body(k) else lit(v,p) for k,v,p in args)
        return (f"<?php\n// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"require 'vendor/autoload.php';\n\n"
                f"$config = WhoisFreaks\\Configuration::getDefaultConfiguration();\n"
                f"$api = new WhoisFreaks\\Api\\{cls}(new GuzzleHttp\\Client(), $config);\n"
                f"list($data, $statusCode, $headers) = $api->{m}WithHttpInfo({pos});\n"
                f'echo "status: " . $statusCode . PHP_EOL;\n'
                f"print_r($data);\n")

    if lang == "swift":
        parts=[]
        for k,v,p in args:
            if is_body(k):
                parts.append(f"{k.split(':')[1]}: {bm}()")
            elif v is None:
                parts.append(f"{k}: nil")          # Swift uses nil, not null
            else:
                parts.append(f"{k}: {lit(v,p)}")
        found_imp = "import Foundation\n" if uses_yesterday else ""
        # The Swift SDK uses async/await (async throws), not completion handlers.
        return (f"// Runnable example: {op['summary']} ({op['method']} {op['path']})\n"
                f"{pcmt_all}\n"
                f"{found_imp}import WhoisFreaks\n\n"
                f"do {{\n"
                f"    let result = try await {cls}.{m}({', '.join(parts)})\n"
                f"    print(result)\n"
                f"}} catch {{\n"
                f"    print(error)\n"
                f"}}\n")

    return "// unsupported\n"

# unify: doc snippets use the same full-signature renderer as runnable files
# (render_example forwards to runnable_example; see its definition above)


def render_example(lang, op):
    # Forwarder: language pages (docs/languages/*.md) and endpoint pages must use
    # the SAME renderer as the runnable example files so inline snippets stay in
    # sync. runnable_example returns just the code string; inline callers expect
    # a (fence, code) tuple, so wrap it with the right syntax-highlight fence.
    FENCE = {"python": "python", "javascript": "javascript", "typescript": "typescript",
             "java": "java", "kotlin": "kotlin", "csharp": "csharp", "ruby": "ruby",
             "go": "go", "php": "php", "swift": "swift"}
    return FENCE.get(lang, ""), runnable_example(lang, op)

def w(path, text):
    p = OUT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + "\n")

def param_table(params):
    rows = ["| Parameter | In | Required | Type | Description |",
            "|-----------|----|----------|------|-------------|"]
    for p in params:
        allowed = f" (one of: {', '.join(map(str, p['enum']))})" if p["enum"] else ""
        req = "yes" if p["required"] else "no"
        rows.append(f"| `{p['name']}` | {p['in']} | {req} | {p['type']} | "
                    f"{(p['desc'] or '').replace('|','\\|')}{allowed} |")
    return "\n".join(rows)

TOTAL_OPS = sum(len(v) for v in OPS.values())
INFO = spec["info"]
# flatten the multi-line spec description into a single clean sentence
DESC1 = " ".join(INFO["description"].split("\n\n")[0].split())

# ---------- endpoints/<tag>.md -----------------------------------------------
for tag, ops in OPS.items():
    body = [f"# {tag}", ""]
    if TAG_DESC := next((t.get("description") for t in spec.get("tags", []) if t.get("name") == tag), None):
        body += [TAG_DESC, ""]
    body += [f"{len(ops)} endpoint(s). All requests require your API key — see "
             f"[Authentication](../authentication.md).", ""]
    for op in ops:
        anchor = op["op_id"] or op["path"]
        body += [f"## {op['summary'] or op['op_id']}", ""]
        body += [f"`{op['method']} {op['path']}`", ""]
        if op["description"]:
            body += [op["description"], ""]
        body += ["**Parameters**", "", param_table(op["params"]), ""]
        # usage example in three common languages
        body += ["**Usage**", ""]
        for lang in ("python", "typescript", "go"):
            fence, code = render_example(lang, op)
            body += [f"<details><summary>{LANGS[lang]['label']}</summary>", "",
                     f"```{fence}", code, "```", "", "</details>", ""]
        body += ["---", ""]
    w(f"docs/endpoints/{slug(tag)}.md", "\n".join(body))

# ---------- endpoints/README.md (catalog) ------------------------------------
cat = ["# Endpoint Reference", "",
       f"The WhoisFreaks API exposes **{TOTAL_OPS} endpoints** across "
       f"**{len(OPS)} categories**. Every endpoint is available in all "
       f"{len(LANGS)} SDKs. Browse by category:", ""]
for tag in OPS:
    cat.append(f"- [{tag}]({slug(tag)}.md) — {len(OPS[tag])} endpoint(s)")
cat += ["", "## Full endpoint list", "",
        "| Category | Method | Path | Operation |",
        "|----------|--------|------|-----------|"]
for tag, ops in OPS.items():
    for op in ops:
        cat.append(f"| {tag} | {op['method']} | `{op['path']}` | `{op['op_id']}` |")
w("docs/endpoints/README.md", "\n".join(cat))

# ---------- authentication.md ------------------------------------------------
auth = f"""# Authentication

Every WhoisFreaks API request requires an **API key**, passed as the `apiKey`
query parameter. Each SDK exposes a configuration hook so you set the key once
and it is attached to every request automatically.

## Get an API key

1. Sign in at <https://billing.whoisfreaks.com>.
2. Copy your API key from the dashboard.
3. Keep it secret — do **not** commit it to source control. Prefer an
   environment variable (e.g. `WHOISFREAKS_API_KEY`).

## Base URLs

| Purpose | Base URL |
|---------|----------|
| Live API lookups | `{spec['servers'][0]['url']}` |
| Database file downloads | `{spec['servers'][1]['url']}` |

## Setting the key per language

""".splitlines()
# reuse the first WHOIS op (falling back to any op) for a per-language auth example
first_op = OPS.get("WHOIS", next(iter(OPS.values())))[0]
for lang in LANG_ORDER:
    fence, code = render_example(lang, first_op)
    auth += [f"### {LANGS[lang]['label']}", "", f"```{fence}", code, "```", ""]
w("docs/authentication.md", "\n".join(auth))

# ---------- languages/<lang>.md ----------------------------------------------
for lang in LANG_ORDER:
    m = LANGS[lang]
    fence_i, inst = install_snippet(lang)
    body = [f"# {m['label']} SDK", "",
            f"- **Registry:** {m['registry']}",
            f"- **Package:** `{m['pkg']}`", "",
            "## Install", "", f"```{fence_i}", inst, "```", "",
            "## Getting Started", "",
            "A complete walkthrough from an empty directory to a running "
            "program:", ""]
    body += getting_started(lang)
    body += ["",
            "## Configure", "",
            f"See [Authentication](../authentication.md) for how to obtain a key. "
            f"Minimal setup:", ""]
    fence_c, code = render_example(lang, first_op)
    body += [f"```{fence_c}", code, "```", "",
             "## Endpoints", "",
             f"All {TOTAL_OPS} endpoints are available. A few common examples "
             f"follow; see the [full endpoint reference](../endpoints/README.md) "
             f"for every operation, its parameters, and response shape.", ""]
    # show one example per category (first op of each tag)
    for tag, ops in OPS.items():
        op = ops[0]
        fence, code = render_example(lang, op)
        body += [f"### {tag}: {op['summary'] or op['op_id']}", "",
                 f"`{op['method']} {op['path']}`", "",
                 f"```{fence}", code, "```", ""]
    w(f"docs/languages/{lang}.md", "\n".join(body))

# ---------- root README ------------------------------------------------------
lang_rows = "\n".join(
    f"| {LANGS[l]['label']} | {LANGS[l]['registry']} | `{LANGS[l]['pkg']}` | "
    f"[Guide](docs/languages/{l}.md) |"
    for l in LANG_ORDER)
cat_rows = "\n".join(f"| [{tag}](docs/endpoints/{slug(tag)}.md) | {len(ops)} |"
                     for tag, ops in OPS.items())

readme = f"""# WhoisFreaks SDK Documentation

Official documentation for the **WhoisFreaks** SDKs — one API, {len(LANGS)}
languages, {TOTAL_OPS} endpoints. Every SDK is generated from the same
[OpenAPI specification](https://whoisfreaks.com/documentation) and published to
its language's standard registry.

> {DESC1}

## Contents

- [Authentication](docs/authentication.md) — get and configure your API key
- [Language guides](#language-guides) — install + usage for each SDK
- [Endpoint reference](docs/endpoints/README.md) — all {TOTAL_OPS} endpoints, grouped by category
- [Runnable examples](examples/README.md) — copy-paste, ready-to-run example for every endpoint in every language

## Language guides

| Language | Registry | Package | Guide |
|----------|----------|---------|-------|
{lang_rows}

## Quick start

Pick your language, install the package, set your API key, and call an endpoint.
Example (Python):

```bash
pip install {LANGS['python']['pkg']}
```

```python
import whoisfreaks
from whoisfreaks import Configuration, ApiClient

config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"
client = ApiClient(config)

result = client.{method_name(first_op['op_id'], 'python')}(domainName="example.com")
print(result)
```

The equivalent for every other language is in its [language guide](#language-guides).

## Endpoint categories

| Category | Endpoints |
|----------|-----------|
{cat_rows}

See the [full endpoint reference](docs/endpoints/README.md) for the complete
list with parameters and per-language examples.

## Authentication at a glance

All requests require an `apiKey` query parameter. Get a key at
<https://billing.whoisfreaks.com>, then configure it once via each SDK's
configuration object — see [Authentication](docs/authentication.md).

Base URLs:

| Purpose | URL |
|---------|-----|
| Live lookups | `{spec['servers'][0]['url']}` |
| Database downloads | `{spec['servers'][1]['url']}` |

## About these docs

These docs are generated from the OpenAPI spec by `scripts/gen_docs.py`, so they
stay in sync with the API. To regenerate after a spec change:

```bash
python3 scripts/gen_docs.py path/to/whoisfreaks-openapi.yaml .
```

## Support

- API docs: <https://whoisfreaks.com/documentation>
- Billing & keys: <https://billing.whoisfreaks.com>
- Email: {INFO.get('contact', {}).get('email', 'support@whoisfreaks.com')}

## License

{spec.get('info', {}).get('license', {}).get('name', 'MIT')} — see individual SDK repositories for details.
"""
w("README.md", readme)

print(f"generated docs for {len(LANGS)} languages and {TOTAL_OPS} endpoints "
      f"across {len(OPS)} categories -> {OUT}")


# ============================================================================
# Runnable, copy-paste examples: one file per endpoint per language.
# These use the FULL method signature (all params positional where the language
# requires it, passing null/None for optionals) so they compile/run as-is.
# ============================================================================
EXT = {"python":"py","javascript":"js","typescript":"ts","java":"java",
       "kotlin":"kt","csharp":"cs","ruby":"rb","go":"go","swift":"swift","php":"php"}

def write_examples():
    count=0
    for tag, ops in OPS.items():
        for op in ops:
            P=_pascal(op["op_id"])
            for lang in LANG_ORDER:
                code=runnable_example(lang, op)
                w(f"examples/{lang}/{P}.{EXT[lang]}", code)
                count+=1
    # index
    idx=["# Runnable Examples","",
         f"Copy-paste, ready-to-run examples for **every one of the {TOTAL_OPS} "
         f"endpoints** in **all {len(LANGS)} languages** ({count} files).","",
         "Set `YOUR_API_KEY` to your key (from <https://billing.whoisfreaks.com>) "
         "and run. Layout: `examples/<language>/<Operation>.<ext>`.","",
         "| Endpoint | Operation | Example file (per language) |",
         "|----------|-----------|------------------------------|"]
    for tag, ops in OPS.items():
        for op in ops:
            P=_pascal(op["op_id"])
            links=" · ".join(f"[{LANGS[l]['label']}]({l}/{P}.{EXT[l]})" for l in LANG_ORDER)
            idx.append(f"| {op['summary']} | `{op['op_id']}` | {links} |")
    # per-language example index
    for lang in LANG_ORDER:
        li=[f"# {LANGS[lang]['label']} — Runnable Examples","",
            f"Install: see the [{LANGS[lang]['label']} guide](../../docs/languages/{lang}.md). "
            f"Set `YOUR_API_KEY` and run any file below.",""]
        for tag, ops in OPS.items():
            li.append(f"## {tag}")
            for op in ops:
                P=_pascal(op["op_id"])
                li.append(f"- [`{P}.{EXT[lang]}`]({P}.{EXT[lang]}) — {op['summary']} (`{op['method']} {op['path']}`)")
            li.append("")
        w(f"examples/{lang}/README.md", "\n".join(li))
    w("examples/README.md","\n".join(idx))
    return count

_ex = write_examples()
print(f"wrote {_ex} runnable example files")
