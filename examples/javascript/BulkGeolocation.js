// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
// whoisfreaks-js is CommonJS — import default then destructure
import pkg from "whoisfreaks-js";
const { Configuration, GeolocationApi } = pkg;
// (CommonJS alternative: const { Configuration, GeolocationApi } = require("whoisfreaks-js");)

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.bulkGeolocationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
