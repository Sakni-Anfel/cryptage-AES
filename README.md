#  ESP32 Secure IoT Sensor Node — AES-256 + MQTT

A MicroPython-based IoT project running on an **ESP32** that reads temperature and humidity from a **DHT22** sensor, encrypts the data using **AES-256-CBC** encryption, displays live readings on an **SSD1306 OLED screen**, and publishes the encrypted payload over **MQTT**.

>  Fully simulated on [Wokwi](https://wokwi.com/projects/461731017344964609) — no hardware required to run it.

---

##  Demo

### Wokwi Simulation
<img width="740" height="474" alt="Wokwi simulation" src="https://github.com/user-attachments/assets/f57d3236-88da-4f20-bfb0-8cb324a825c4" />

### Circuit & OLED Output
<img width="658" height="482" alt="Circuit running" src="https://github.com/user-attachments/assets/06cf1306-6bfc-49d2-b643-05afd2159e0d" />

**OLED display shows:**
- Temperature in °C
- Humidity in %
- First 14 hex characters of the encrypted payload

**Serial monitor output:**
```
Input: 41.9 40.0
Using AES256-CBC cipher
Encrypted: b'\x9a\xbe\xef\xc1xB\x17\x9d\x80\x88\x110\x04\x84q\xe1'
```

---

## Data flow

1. DHT22 reads temperature & humidity every 2 seconds
2. Raw data is padded and encrypted with AES-256-CBC (`ucryptolib`)
3. Encrypted payload is published to MQTT topic `CRYPT/AES`
4. OLED displays live sensor values + truncated encrypted hex

---

##  Hardware

| Component | Description |
|-----------|-------------|
| ESP32 DevKit | Main microcontroller (Wi-Fi enabled) |
| DHT22 | Temperature & humidity sensor — GPIO 14 |
| SSD1306 OLED | 128×64 I2C display — SDA: GPIO 21, SCL: GPIO 22 |

---

##  Dependencies

| Library | Purpose |
|---------|---------|
| `ucryptolib` | Built-in MicroPython AES encryption |
| `umqtt.simple` | MQTT client for MicroPython |
| `ssd1306` | OLED display driver |
| `dht` | DHT22 sensor driver |
| `network` | Wi-Fi management |

---

## Getting Started

### Run on Wokwi (no hardware needed)

👉 [**Click here to open the live simulation**](https://wokwi.com/projects/461731017344964609)

Just press the green ▶ button — no setup required.

### Run on real hardware

1. Flash MicroPython firmware onto your ESP32
2. Upload `main.py` and `ssd1306.py` using [Thonny](https://thonny.org/) or `mpremote`
3. Update Wi-Fi credentials in `main.py`:
```python
sta_if.connect('YOUR_SSID', 'YOUR_PASSWORD')
```
4. Optionally change the AES key and IV:
```python
key = b'your-32-byte-key-here-----------'  # must be exactly 32 bytes
iv  = b'your-16-byte-iv-'                  # must be exactly 16 bytes
```
5. Monitor output via serial terminal at 115200 baud

---

##  Security Details

| Parameter | Value |
|-----------|-------|
| Algorithm | AES-256-CBC |
| Key size | 256 bits (32 bytes) |
| IV size | 128 bits (16 bytes) |
| Padding | Space padding to 16-byte block boundary |
| Library | `ucryptolib` (built-in MicroPython) |

>  **Note:** The key and IV are hardcoded for demonstration purposes. In a production system, use secure key exchange and a random IV per message.

---

##  MQTT

| Parameter | Value |
|-----------|-------|
| Broker | `test.mosquitto.org` (public) |
| Topic | `CRYPT/AES` |
| Payload | AES-256-CBC encrypted string |

Monitor published messages with any MQTT client:
```bash
mosquitto_sub -h test.mosquitto.org -t "CRYPT/AES"
```

---

## Project Structure

```
cryptage-AES/
├── main.py          # Main application logic
├── ssd1306.py       # OLED display driver
├── diagram.json     # Wokwi circuit diagram
└── README.md
```

---

##  What This Project Demonstrates

- Symmetric encryption (AES-256-CBC) on a microcontroller
- Secure IoT data transmission over MQTT
- I2C peripheral management (OLED display)
- Real-time sensor data acquisition and display
- MicroPython development on ESP32

---

##  License

MIT License — feel free to use, modify, and distribute.

---

##  Author

**Anfel Sakni** — Embedded Systems Engineering Student
 [GitHub](https://github.com/Sakni-Anfel)
