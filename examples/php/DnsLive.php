<?php
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dnsLiveWithHttpInfo("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
