<?php
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPSecurityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpSecurityWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
