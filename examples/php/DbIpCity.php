<?php
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpCityWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
