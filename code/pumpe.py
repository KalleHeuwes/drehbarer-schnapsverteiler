import RPi.GPIO as GPIO
import time
import datetime
import sys

def log(inText):
    c = datetime.datetime.now()
    current_time = c.strftime('%H:%M:%S')
    print(current_time + " " + inText)
    
def pumpe_an():
    log(f"* bin in Pumpe an...")
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)

def pumpe_aus():
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)
    
if __name__ == "__main__":
    fuelldauer = float(sys.argv[1])

log("* 1...")    
RELAIS_PIN = 14         # GPIO-Pin für das Relais
GPIO.setmode(GPIO.BCM)  # GPIO-Modus setzen
log("* 2...")    
GPIO.setup(RELAIS_PIN, GPIO.OUT)
log("* 3...")    
pumpe_aus()

try:
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

finally:
    GPIO.cleanup()
