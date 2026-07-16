// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
// whoisfreaks-js is CommonJS; apiKey is set once on the ApiClient
import pkg from "whoisfreaks-js";
const { ApiClient, GeolocationApi } = pkg;
// or:  const { ApiClient, GeolocationApi } = require("whoisfreaks-js");

const client = ApiClient.instance;
client.authentications["ApiKeyAuth"].apiKey = "YOUR_API_KEY";  // set once
const api = new GeolocationApi(client);

api.geolocation("8.8.8.8")
  .then(data => console.log(data))
  .catch(err => console.error(err));
