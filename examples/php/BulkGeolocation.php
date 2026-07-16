<?php
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\GeolocationApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkGeolocation(new WhoisFreaks\Model\BulkGeolocationRequest());
print_r($result);
