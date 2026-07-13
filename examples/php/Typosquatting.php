<?php
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\TyposquattingApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->typosquattingWithHttpInfo("YOUR_API_KEY", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
