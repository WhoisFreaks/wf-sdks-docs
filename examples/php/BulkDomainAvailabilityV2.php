<?php
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DomainAvailabilityApi(new GuzzleHttp\Client(), $config);
$result = $api->bulkDomainAvailabilityV2(new WhoisFreaks\Model\BulkDomainAvailabilityRequest(), null, null);
print_r($result);
