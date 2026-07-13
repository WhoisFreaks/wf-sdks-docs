// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, GeolocationApi } = pkg;
// or:  const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

const api = new GeolocationApi();   // uses ApiClient.instance

api.bulkGeolocation("YOUR_API_KEY", {})
  .then(data => console.log(data))
  .catch(err => console.error(err));
