<?php
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesSubdomainsApi(new GuzzleHttp\Client(), $config);
$result = $api->dbSubdomainsDaily((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);
