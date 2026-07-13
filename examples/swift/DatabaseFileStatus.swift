// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import WhoisFreaks

do {
    let result = try await AccountAPI.databaseFileStatus()
    print(result)
} catch {
    print(error)
}
