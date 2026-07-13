<?php
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\SubdomainsApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->subdomainsWithHttpInfo("YOUR_API_KEY", "example.com", "2000-01-01", (new DateTime("today"))->format("Y-m-d"), null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
