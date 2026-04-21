from machine import Pin, I2C,Timer
from time import sleep
import ssd1306
import network 
import dht
from ucryptolib import aes

from umqtt.simple import MQTTClient
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    sleep(0.1)
print(" Connected!")
print("Network config:", sta_if.ifconfig())
tim=Timer(1)
MQTT_CLIENT_ID="AES"
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC_AES = "CRYPT/AES"
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.connect()

key = b'anfel-fgh-145-lkj-anfel-45-sakni'
iv = b'secret-iv-123456' 

MODE_CBC = 2


i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sns=dht.DHT22(Pin(14))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)



while True:
    print(len(key))
    sns.measure()
    tmp=sns.temperature()
    hum=sns.humidity()
    temp_f=tmp*(9/5)+32.0
    plain = str(tmp) + " " + str(hum)
    print('Input:{}'.format(plain))
    print("Using AES{}-CTR cipher".format(len(key) * 8))
    oled.fill(0);
    oled.text("T:{:.1f}C, H:{:.}%".format(tmp,hum),0, 10)      
    oled.show()
    cipher = aes(key, MODE_CBC, iv)
    padded = plain + " " * (16 - len(plain) % 16)
    encrypted = cipher.encrypt(padded.encode())
    print('Encrypted: {}'.format(encrypted))
    client.publish(MQTT_TOPIC_AES, str(encrypted))
    oled.text("E:{}".format(encrypted.hex()[:14]),0, 20)
    oled.show()

    sleep(2) 