<?php
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dnsBulkWithHttpInfo("YOUR_API_KEY", "value", new WhoisFreaks\Model\DnsBulkRequest(), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
