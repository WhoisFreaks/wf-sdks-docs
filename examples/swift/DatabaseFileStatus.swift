// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import WhoisFreaks

AccountAPI.DatabaseFileStatus() { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
