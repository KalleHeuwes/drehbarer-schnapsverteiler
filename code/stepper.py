import RPi.GPIO as GPIO
import time

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

def motor_steuern(steps, delay=0.002):
    """Bewegt den Motor um eine bestimmte Anzahl von Schritten"""
    if steps < 0:
        seq.reverse()  # Drehrichtung umkehren
        steps = -steps

    for _ in range(steps):
        for step in seq:
            for pin, val in zip(motor_pins, step):
                GPIO.output(pin, val)
            time.sleep(delay)

try:
    print("Motor dreht sich vorwärts...")
    motor_steuern(512)  # 512 Schritte = ca. eine Umdrehung
    time.sleep(1)

    print("Motor dreht sich rückwärts...")
    motor_steuern(-512)

finally:
    GPIO.cleanup()
