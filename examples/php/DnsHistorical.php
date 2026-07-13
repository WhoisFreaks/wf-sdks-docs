<?php
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dnsHistoricalWithHttpInfo("YOUR_API_KEY", "example.com", "value", null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
