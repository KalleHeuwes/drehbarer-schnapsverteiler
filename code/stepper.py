import RPi.GPIO as GPIO
import time
import sys
import datetime
import subprocess


if __name__ == "__main__":
    anzahlPinnchen = int(sys.argv[1])
    fuellmenge = float(sys.argv[2])
    fuelldauer = fuellmenge / 10

# GPIO-Modus setzen
GPIO.setmode(GPIO.BCM)

# Pins für den ULN2003 Motor Driver
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# RELAIS_PIN = 4  # GPIO-Pin für die Pumpe
# GPIO.setup(RELAIS_PIN, GPIO.OUT)
# GPIO.output(RELAIS_PIN, 0)

# Pin-Setup
motor_pins = [IN1, IN2, IN3, IN4]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Schrittsequenz für den Motor (Halbschritt)
seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def log(inText):
    c = datetime.datetime.now()
    current_time = c.strftime('%H:%M:%S')
    print(current_time + " " + inText)
    
def motor_steuern(steps, delay=0.001):
    """Bewegt den Motor um eine bestimmte Anzahl von Schritten"""
    log("Fahre zum nächsten Pinnchen ...")
    if steps < 0:
        seq.reverse()  # Drehrichtung umkehren
        steps = -steps

    for _ in range(steps):
        for step in seq:
            for pin, val in zip(motor_pins, step):
                GPIO.output(pin, val)
            time.sleep(delay)

def pumpe(delay):
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)
    time.sleep(delay)
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)
    log("Pumpe aus")
    
def pumpe_an():
    GPIO.output(RELAIS_PIN, GPIO.HIGH)  # Relais aktivieren (Pumpe EIN)

def pumpe_aus():
    GPIO.output(RELAIS_PIN, GPIO.LOW)   # Relais deaktivieren (Pumpe AUS)
    
try:
       
    for x in range(anzahlPinnchen):
        log(f"Befülle Pinnchen {x + 1} mit {fuellmenge} ml für {fuelldauer} Sekunden ...")
        subprocess.run(["python3", "pumpe.py", "2"])
        # pumpe(fuelldauer)
        # time.sleep(2)
        #time.sleep(fuelldauer)
        #pumpe_an()
        #time.sleep(fuelldauer)
        #print("Pumpe aus")
        #pumpe_aus()
        motor_steuern(int(512/ anzahlPinnchen))
    
    # print("Motor dreht sich vorwärts...")
    # motor_steuern(128)  # 512 Schritte = ca. eine Umdrehung
    # time.sleep(1)

    # print("Motor dreht sich rückwärts...")
    # motor_steuern(-256)

finally:
    GPIO.cleanup()
