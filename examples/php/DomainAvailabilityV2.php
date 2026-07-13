<?php
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->domainAvailabilityV2WithHttpInfo("YOUR_API_KEY", "example.com", null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
