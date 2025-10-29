# 🌡️ ESP8266 + DHT22 + SSD1306 OLED — Temperature & Humidity Monitor (MicroPython)

## 🧠 Overview
This project reads **temperature** and **humidity** data from a **DHT22 sensor** and displays it on a **128x64 SSD1306 OLED display** using **MicroPython** on an **ESP8266** board.  
A minimal, reliable setup for environmental monitoring — ideal for IoT dashboards and smart home systems.

---

## ⚙️ Hardware Setup

| Component | ESP8266 Pin | Description |
|------------|-------------|-------------|
| DHT22 Data | GPIO2 (D4)  | Temperature & humidity sensor data |
| OLED SDA   | GPIO4 (D2)  | I2C data line |
| OLED SCL   | GPIO5 (D1)  | I2C clock line |
| VCC        | 3.3V        | Power supply |
| GND        | GND         | Common ground |

**Connections:**
- DHT22 VCC → 3.3V  
- DHT22 GND → GND  
- DHT22 DATA → GPIO2 (D4)  
- OLED SDA → GPIO4 (D2)  
- OLED SCL → GPIO5 (D1)  

---

## 🧩 Code

```python
from machine import Pin, I2C
import ssd1306
import dht
import utime

# OLED I2C setup
i2c = I2C(sda=Pin(4), scl=Pin(5))  # D1 = SCL, D2 = SDA
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# DHT22 sensor setup
dh = dht.DHT22(Pin(2))  # D4 = GPIO2 (Data)

while True:
    dh.measure()
    tem = dh.temperature()
    hum = dh.humidity()
    utime.sleep_ms(2000)

    # Clear OLED and display readings
    display.fill(0)
    display.text('Temperature:', 0, 0, 1)
    display.text(str(tem), 10, 15, 1)
    display.text('Humidity:', 0, 30, 1)
    display.text(str(hum), 10, 45, 1)
    display.show()

    # Print to serial monitor
    print('Humidity:', hum, 'Temperature:', tem)
