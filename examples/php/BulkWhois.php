<?php
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->bulkWhoisWithHttpInfo("YOUR_API_KEY", new WhoisFreaks\Model\BulkWhoisRequest(), null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
