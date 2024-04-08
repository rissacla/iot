#include <WiFi.h>
#include <WebServer.h>
#include <M5StickCPlus.h>

// Replace with your WiFi network's details
const char* ssid = "your-SSID";
const char* password = "your-password";

// Create a web server on port 80
WebServer server(80);

// Sensor and measurement parameters
const int sensorPin = 36; 
const float voltageSupply = 3.3;
const int analogResolution = 4095;
float calibrationFactor = 0.265; // Adjust this based on your calibration process

// Global variables to store RMS measurements
float rmsVoltage = 0.0;
float rmsCurrent = 0.0;
int chargerSelection = 1; // Start with charger 1 as default

void setup() {
  M5.begin();
  Serial.begin(115200);
  pinMode(sensorPin, INPUT);
  pinMode(25, INPUT); // If not used, consider ensuring it's correctly configured or removing

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  // Setup route handlers for the web server
  server.on("/", handleRoot); // Serve the webpage with Ajax for dynamic updates
  server.on("/data", handleData); // Serve RMS data and efficiency in JSON format
  server.on("/toggleCharger", []() {
  chargerSelection = chargerSelection == 1 ? 2 : 1; // Toggle charger selection
  server.send(200, "text/plain", String(chargerSelection));
  });
  
  // Start the server
  server.begin();
}

void loop() {
  server.handleClient(); // Handle client requests to the server
  
  // Measure RMS voltage and current
  measureRMS();

  // Introduce a short delay for readability and to pace measurements
  delay(1000);
}

void measureRMS() {
  unsigned long sampleTime = 18.18; // Adjust based on your target frequency
  unsigned long startSampleTime = millis();
  float sum = 0;
  int sampleCount = 0;

  while (millis() - startSampleTime < sampleTime) {
    int sensorValue = analogRead(sensorPin);
    float voltage = (sensorValue * voltageSupply / analogResolution) - (voltageSupply / 2.0);
    sum += sq(voltage);
    sampleCount++;
  }

  rmsVoltage = sqrt(sum / sampleCount) * calibrationFactor;
  rmsCurrent = (rmsVoltage / 0.2); // Convert RMS voltage to RMS current using the sensor spec
}

void handleRoot() {
  String message = "<html><head><title>M5StickC Plus Readings</title>";
  message += "<script>";
  message += "setInterval(function() {";
  message += "fetch('/data').then(response => response.json()).then(data => {";
  message += "document.getElementById('power').innerHTML = data.power + ' kW';";
  message += "document.getElementById('efficiency').innerHTML = data.efficiency + ' %';";
  message += "});";
  message += "}, 1000);"; // Update every second
  message += "function toggleCharger() {";
  message += "fetch('/toggleCharger').then(response => response.text()).then(data => {";
  message += "document.getElementById('chargerBtn').innerHTML = 'Charger ' + data;";
  message += "});";
  message += "}";
  message += "</script></head><body>";
  message += "<h1>RMS Readings</h1>";
  message += "<p>Power Consumption: <span id='power'></span></p>";
  message += "<p>Efficiency: <span id='efficiency'></span></p>";
  message += "<button onclick='toggleCharger()' id='chargerBtn'>Charger 1</button>";
  message += "</body></html>";

  server.send(200, "text/html", message);
}


void handleData() {
  float vRMS = 240.0; // Mains RMS voltage
  float pInKWh = vRMS * rmsCurrent / 1000; // Input power (W)
  
  float vOut, iOut, pOutKWh;

  if (chargerSelection == 1) {
    // Charger 1 specifications
    vOut = 19.0;
    iOut = 7.1;
  } else {
    // Charger 2 specifications
    vOut = 19.0;
    iOut = 3.42;
  }
  
  pOutKWh = vOut * iOut / 1000; // Output power (W)
  
  // Calculate efficiency
  float efficiency = (pOutKWh / pInKWh) * 100.0; // Efficiency (%)
  
  char json[200];
  snprintf(json, sizeof(json), "{\"power\": \"%.3f\", \"efficiency\": \"%.2f%\"}", pInKWh, efficiency);
  server.send(200, "application/json", json);
}