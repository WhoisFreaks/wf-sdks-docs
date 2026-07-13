<?php
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\ASNWHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->asnWhoisWithHttpInfo("YOUR_API_KEY", "AS15169", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
