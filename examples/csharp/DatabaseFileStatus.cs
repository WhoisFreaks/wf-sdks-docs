// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DatabaseFileStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new AccountApi(config);
        var resp = api.DatabaseFileStatusWithHttpInfo();
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
