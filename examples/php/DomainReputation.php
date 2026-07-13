<?php
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\DomainReputationApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->domainReputationWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
