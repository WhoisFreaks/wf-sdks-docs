<?php
// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbDroppedWithHttpInfo("YOUR_API_KEY", false, (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
