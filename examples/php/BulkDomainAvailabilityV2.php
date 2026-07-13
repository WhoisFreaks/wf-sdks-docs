<?php
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->bulkDomainAvailabilityV2WithHttpInfo("YOUR_API_KEY", new WhoisFreaks\Model\BulkDomainAvailabilityRequest(), null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
