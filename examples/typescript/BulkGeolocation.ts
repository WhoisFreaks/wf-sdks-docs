// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.bulkGeolocationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);
