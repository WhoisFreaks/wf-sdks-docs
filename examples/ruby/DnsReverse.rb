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
