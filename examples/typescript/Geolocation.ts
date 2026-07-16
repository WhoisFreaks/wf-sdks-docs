// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.geolocation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);
