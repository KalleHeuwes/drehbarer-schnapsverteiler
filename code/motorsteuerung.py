import RPi.GPIO as GPIO
import time
import sys
import datetime
import subprocess

if __name__ == "__main__":
    schritte = int(sys.argv[1])

# GPIO-Modus setzen
GPIO.setmode(GPIO.BCM)

# Pins für den ULN2003 Motor Driver
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

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

try:
    motor_steuern(schritte)                     # 512 Schritte = ca. eine Umdrehung

finally:
    GPIO.cleanup()
