#include <M5StickCPlus.h>
#include <WiFi.h>


void setup() {
  M5.begin();
  Serial.begin(115200);
  delay(1000);

  uint8_t mac[6];
  WiFi.macAddress(mac);
  
  // Serial.printf("MAC Address: %02X:%02X:%02X:%02X:%02X:%02X\n", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  M5.Lcd.setCursor(0, 20, 2);
  // M5.Lcd.print("MAC Address: %02X:%02X:%02X:%02X:%02X:%02X\n", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  char macAddress[18]; // MAC address has 17 characters plus null terminator
  
  sprintf(macAddress, "%02X%02X%02X%02X%02X%02X",
  mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
  
  M5.Lcd.print("MAC Address: ");
  M5.Lcd.print(macAddress);
}

void loop() {
  // Empty loop
}
