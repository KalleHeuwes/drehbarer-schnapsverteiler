import gc9a01
from time import sleep
from PIL import Image, ImageDraw

# Display initialisieren
disp = gc9a01.GC9A01(
    spi_bus=0, spi_device=0, gpio_dc=25, gpio_reset=24, gpio_backlight=None
)

# Testbild zeichnen
image = Image.new("RGB", (240, 240), "black")
draw = ImageDraw.Draw(image)
draw.ellipse((60, 60, 180, 180), outline="red", width=5)

disp.display(image)

sleep(10)
