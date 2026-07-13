<?php
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->geolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
