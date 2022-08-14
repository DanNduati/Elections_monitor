import machine
import network
import ujson
import urequests
import utime

import config
import ssd1306

# Network settings
wifi_ssid = config.WIFI_SSID
wifi_password = config.WIFI_PASSWD

# Election data api endpoint url
URL = "http://192.168.100.11:8000/election/"
SLEEP_TIME = 900000

# Oled Display
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        oled.text("Connecting", 22, 10)
        oled.show()
        oled.text("to WI-FI", 22, 30)
        oled.show()
        oled.fill(0)
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_password)
        while not sta_if.isconnected():
            utime.sleep(0.5)
    print(f"Connected to {wifi_ssid}")
    print("Network config:", sta_if.ifconfig())


def get_data(url):
    try:
        resp = urequests.get(url)
        parsed = ujson.loads(resp.text)
    except Exception as e:
        raise e
    else:
        return parsed["data"]


# Continous horizontal scroll
# Source: https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/
def scroll_screen_in_out(screen):
    for i in range(0, (oled_width + 1) * 2, 1):
        for line in screen:
            oled.text(line[2], -oled_width + i, line[1])
        oled.show()
        if i != oled_width:
            oled.fill(0)


def display_data(candidates_data):
    screen = []
    for num, candidate_data in enumerate(candidates_data):
        screen.append(
            [
                0,
                num * 16,
                f"{num+1}.{candidate_data['CandidateName'].split(' ')[1]}: {candidate_data['Votes']}({candidate_data['Percentage']})",
            ]
        )
    # scroll the results horizontally thrice
    for i in range(3):
        scroll_screen_in_out(screen)


def main():
    connect_wifi()
    data = get_data(url=URL)
    display_data(data)


main()
# put the device to deepsleep for 5 minutes
print("Entering Deepsleep")
machine.deepsleep(SLEEP_TIME)
