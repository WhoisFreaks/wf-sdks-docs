<?php
// Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
// Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (string (one of: historical, reverse), required)
//   - domainName (string, required): Required for historical lookup
//   - keyword (string, optional): For reverse — domain keyword search
//   - email (string, optional): For reverse — registrant email search
//   - owner (string, optional): For reverse — registrant name search
//   - company (string, optional): For reverse — company name search
//   - mode (string (one of: default, mini), optional)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->whoisHistoricalOrReverseWithHttpInfo("YOUR_API_KEY", "historical", "example.com", true, null, null, null, null, null, null, null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);
