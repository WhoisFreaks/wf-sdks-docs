// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.bulkGeolocation({ bulkGeolocationRequest: {} });
  console.log(result);
}
main().catch(console.error);
