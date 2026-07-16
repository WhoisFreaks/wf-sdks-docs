<?php
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
$result = $api->ipReputation("8.8.8.8");
print_r($result);
