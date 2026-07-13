<?php
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPSecurityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpSecurityStatusWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
