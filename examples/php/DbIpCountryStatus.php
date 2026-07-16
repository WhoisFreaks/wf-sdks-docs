<?php
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesIPGeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->dbIpCountryStatus();
print_r($result);
