<?php
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesNewlyRegisteredApi(new GuzzleHttp\Client(), $config);
$result = $api->dbNewlyDns((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);
