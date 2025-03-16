import RPi.GPIO as GPIO
import time
import datetime
import sys
    
if __name__ == "__main__":
    fuelldauer = float(sys.argv[1])
    
def log(inText):
    c = datetime.datetime.now()
    current_time = c.strftime('%H:%M:%S')
    print(current_time + " " + inText)
    
def pumpe(val):
    GPIO.setmode(GPIO.BCM)  # GPIO-Modus setzen
    GPIO.setup(RELAIS_PIN, GPIO.OUT)
    GPIO.output(RELAIS_PIN, val)   # Relais aktivieren/ deaktivieren
    GPIO.cleanup()
    
def pumpe_an():
    pumpe(GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)

def pumpe_aus():
    pumpe(GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)

RELAIS_PIN = 14         # GPIO-Pin für das Relais


if fuelldauer > 0:
    log(f"* Pumpe startet für {fuelldauer} Sekunden...")
    pumpe_an()
    time.sleep(fuelldauer)
    pumpe_aus()
if fuelldauer == 0:
    pumpe_aus()
if fuelldauer < 0:
    log(f"* Pumpenfunktion trocken simuliert für {abs(fuelldauer)} Sekunde(n)...")
    time.sleep(abs(fuelldauer))
    log("Pumpe aus")

