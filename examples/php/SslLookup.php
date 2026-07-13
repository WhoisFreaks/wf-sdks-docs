<?php
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\SSLApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->sslLookupWithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
