<?php
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesASNWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbAsnWhoisStatusWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
