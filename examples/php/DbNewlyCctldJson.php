<?php
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbNewlyCctldJsonWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
