import time

import RPi.GPIO as GPIO

class TurningKnob:
    def __init__(self, clk_pin, dt_pin):
        self.clk_pin = clk_pin
        self.dt_pin = dt_pin
        self.counter = 0
        self.clk_last_state = None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.clk_last_state = GPIO.input(self.clk_pin)

    def update(self):
        clk_state = GPIO.input(self.clk_pin)
        dt_state = GPIO.input(self.dt_pin)

        if clk_state != self.clk_last_state:
            if dt_state != clk_state:
                self.counter += 1
            else:
                self.counter -= 1

        self.clk_last_state = clk_state

    def get_counter(self):
        return self.counter

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    knob = TurningKnob(clk_pin=17, dt_pin=18)

    try:
        while True:
            knob.update()
            print("Counter:", knob.get_counter())
            time.sleep(0.1)
    except KeyboardInterrupt:
        knob.cleanup()