import RPi.GPIO as GPIO
import time
import datetime
import sys

def log(inText):
    c = datetime.datetime.now()
    current_time = c.strftime('%H:%M:%S')
    print(current_time + " " + inText)
    
def pumpe_an():
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)

def pumpe_aus():
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)
    
if __name__ == "__main__":
    fuelldauer = float(sys.argv[1])
    
GPIO.setmode(GPIO.BCM)  # GPIO-Modus setzen
RELAIS_PIN = 14          # GPIO-Pin für das Relais
GPIO.setup(RELAIS_PIN, GPIO.OUT)

try:
    
    if fuelldauer > 0:
        log(f"* Pumpe startet für {fuelldauer} Sekunden...")
        pumpe_an()
        time.sleep(fuelldauer)
        pumpe_aus()
    else:
        log(f"* Pumpenfunktion trocken simuliert für 1 Sekunde...")
        time.sleep(1)
        log("Pumpe aus")

finally:
    GPIO.cleanup()
