<?php
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration()
    ->setApiKey("apiKey", "YOUR_API_KEY");  // set once
$api = new WhoisFreaks\Api\DatabasesThreatFeedApi(new GuzzleHttp\Client(), $config);
$result = $api->downloadThreatFeedPhishingSample();
print_r($result);
