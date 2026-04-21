# cryptage-AES
IoT sensor node using ESP32 that reads DHT22 temperature &amp; humidity data, encrypts it with AES-CBC, displays it on an OLED screen, and publishes it over MQTT.

A MicroPython-based IoT project simulated on Wokwi, built around an ESP32 microcontroller. The device reads temperature and humidity from a DHT22 sensor, encrypts the data using AES-CBC (256-bit) encryption via ucryptolib, and publishes the encrypted payload to a public MQTT broker (test.mosquitto.org). Sensor readings are also displayed in real time on an SSD1306 OLED screen. Designed to demonstrate secure data transmission in embedded/IoT systems.
  -Fully simulated on Wokwi — no hardware required to run it. https://wokwi.com/projects/461731017344964609

  #wokwi simulation
  <img width="740" height="474" alt="image" src="https://github.com/user-attachments/assets/f57d3236-88da-4f20-bfb0-8cb324a825c4" />
  #circuit
  <img width="658" height="482" alt="image" src="https://github.com/user-attachments/assets/06cf1306-6bfc-49d2-b643-05afd2159e0d" />

-OLED display shows:
Temperature in °C
Humidity in %
First 14 hex characters of the encrypted payload .
-Serial monitor output:
Input:41.9 40.0
Using AES256-CTR cipher
Encrypted: b'\x9a\xbe\xef\xc1xB\x17\x9d\x80\x88\x110\x04\x84q\xe1

-Data flow:
DHT22 reads temperature & humidity every 2 seconds
Raw data is padded and encrypted with AES-256-CBC (ucryptolib)
Encrypted payload is published to MQTT topic CRYPT/AES
OLED displays live sensor values + truncated encrypted hex

-Hardware
ESP32 DevKitMain: microcontroller (Wi-Fi enabled)
DHT22 : Temperature & humidity sensor — GPIO 14
SSD1306 OLED128×64 :  I2C display — SDA: GPIO 21, SCL: GPIO 22

-Dependencies:
ucryptolib : Built-in MicroPython AES encryption
umqtt.simple : MQTT client for MicroPython
ssd1306OLED : driver
dht : DHT22 sensor driver
network : Wi-Fi management
