<?php
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->ipReputationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
