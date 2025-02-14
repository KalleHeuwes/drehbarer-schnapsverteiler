import RPi.GPIO as GPIO
import time
import sys

if __name__ == "__main__":
    fuelldauer = float(sys.argv[1])
RELAIS_PIN = 4  # GPIO-Pin für das Relais

# GPIO-Modus setzen
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAIS_PIN, GPIO.OUT)

def pumpe_an():
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)

def pumpe_aus():
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)

try:
    print(f"Pumpe startet für {fuelldauer} Sekunden...")
    pumpe_an()
    time.sleep(fuelldauer)
    print("Pumpe aus")
    pumpe_aus()

finally:
    GPIO.cleanup()
