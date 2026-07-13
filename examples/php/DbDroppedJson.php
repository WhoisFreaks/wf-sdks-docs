<?php
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbDroppedJsonWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
