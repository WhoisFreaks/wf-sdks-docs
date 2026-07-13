<?php
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dnsReverseWithHttpInfo("YOUR_API_KEY", "value", "a", true, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
