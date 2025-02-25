from gpiozero import RotaryEncoder, Button
from signal import pause

# GPIO-Pins für den Encoder (CLK, DT) und den Taster (SW)
encoder = RotaryEncoder(9, 10, wrap=True)
button = Button(11)  # GPIO 11 für den Taster

def drehen():
    print(f"Position: {encoder.value}")

def gedrueckt():
    print("Knopf gedrückt!")

encoder.when_rotated = drehen
button.when_pressed = gedrueckt  # Callback für Tastendruck

pause()  # Lässt das Programm laufen
