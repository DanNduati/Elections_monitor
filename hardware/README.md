<h1 align="center"> Presidential Elections Monitor Hardware</h1>

The hardware consists of:
1. [ESP32](https://www.espressif.com/en/products/socs/esp32)
2. SSD1306 OLED Display

## How does it work
The esp32 runs micropython firmware that basically does the following:
### 1. Connects to a wifi
<p align="center">
    <img height=500 src="../images/hw_2.jpg">
</p>

### 2. Pools data presidential tally data from our API
### 3. Displays the data on the oled display
<p align="center">
    <img height=500 src="../images/hw_3.jpg">
</p>

### 4. Put the device to sleep for 30 minutes

Simple right!
