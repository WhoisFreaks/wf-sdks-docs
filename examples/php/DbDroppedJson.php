<?php
// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesExpiringDroppedApi(new GuzzleHttp\Client(), $config);
$result = $api->dbDroppedJson((new DateTime("yesterday"))->format("Y-m-d"), null);
print_r($result);
