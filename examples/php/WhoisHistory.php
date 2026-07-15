<?php
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->whoisHistoryWithHttpInfo("YOUR_API_KEY", "example.com", null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
