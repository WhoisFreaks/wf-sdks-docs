# Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DNSApi.new
result = api.dns_reverse("value", "a", true)
puts result
