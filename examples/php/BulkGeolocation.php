<?php
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->bulkGeolocationWithHttpInfo("YOUR_API_KEY", new WhoisFreaks\Model\BulkGeolocationRequest());
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
