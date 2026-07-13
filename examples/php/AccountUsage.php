<?php
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->accountUsageWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
