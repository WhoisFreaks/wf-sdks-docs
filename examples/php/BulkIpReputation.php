<?php
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->bulkIpReputationWithHttpInfo("YOUR_API_KEY", new WhoisFreaks\Model\BulkGeolocationRequest());
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
