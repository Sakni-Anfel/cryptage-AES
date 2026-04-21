# cryptage-AES
IoT sensor node using ESP32 that reads DHT22 temperature &amp; humidity data, encrypts it with AES-CBC, displays it on an OLED screen, and publishes it over MQTT.

A MicroPython-based IoT project simulated on Wokwi, built around an ESP32 microcontroller. The device reads temperature and humidity from a DHT22 sensor, encrypts the data using AES-CBC (256-bit) encryption via ucryptolib, and publishes the encrypted payload to a public MQTT broker (test.mosquitto.org). Sensor readings are also displayed in real time on an SSD1306 OLED screen. Designed to demonstrate secure data transmission in embedded/IoT systems.
