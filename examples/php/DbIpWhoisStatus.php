<?php
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesIPWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbIpWhoisStatusWithHttpInfo("YOUR_API_KEY");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
