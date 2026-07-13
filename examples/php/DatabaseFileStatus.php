<?php
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\AccountApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->databaseFileStatusWithHttpInfo();
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
