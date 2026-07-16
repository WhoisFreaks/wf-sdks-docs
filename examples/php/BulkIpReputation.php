<?php
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\IPReputationApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkIpReputation(new WhoisFreaks\Model\BulkIpReputationRequest());
print_r($result);
