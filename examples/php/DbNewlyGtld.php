<?php
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbNewlyGtldWithHttpInfo("YOUR_API_KEY", false, (new DateTime("yesterday"))->format("Y-m-d"), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
