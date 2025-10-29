from machine import Pin
from machine import I2C
import ssd1306
import dht
import utime

i2c = I2C(sda=Pin(4), scl=Pin(5)) #D1 = scl = GPIO5, D2 = sda = GPIO4
display = ssd1306.SSD1306_I2C(128, 64, i2c)
dh = dht.DHT22(machine.Pin(2)) #D4 = Data of DHT22 = GPIO2

while True:
    dh.measure()
    tem = dh.temperature()
    hum = dh.humidity()
    utime.sleep_ms(2000)
    display.fill(0)
    display.text('Temperature:', 0, 0, 1)
    display.text(str(tem), 10, 15, 1)
    display.text('Humidity:', 0, 30, 1)
    display.text(str(hum), 10, 45, 1)
    display.show()
    print('Humidity:',hum, 'TEMPERATURE:',tem)