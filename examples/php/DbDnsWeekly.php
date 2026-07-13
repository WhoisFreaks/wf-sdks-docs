<?php
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DatabasesDNSApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->dbDnsWeeklyWithHttpInfo("YOUR_API_KEY", (new DateTime("yesterday"))->format("Y-m-d"));
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
