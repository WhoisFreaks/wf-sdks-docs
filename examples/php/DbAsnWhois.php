<?php
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesASNWHOISApi(new GuzzleHttp\Client(), $config);
$result = $api->dbAsnWhois((new DateTime("yesterday"))->format("Y-m-d"));
print_r($result);
