<?php
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\IPWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->ipWhoisWithHttpInfo("YOUR_API_KEY", "8.8.8.8", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
