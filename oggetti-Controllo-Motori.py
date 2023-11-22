import RPi.GPIO as GPIO
from time import sleep

class Motor:
    dc = 0
    def __init__(self, EN, IN1, IN2):
        self.EN = EN
        self.IN1 = IN1
        self.IN2 = IN2
    
    def setup(self, freq=50, dc=0):
        GPIO.setup(self.EN, GPIO.OUT)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.EN, freq) # Hz
        self.dc = dc
        self.pwm.start(dc)

    def stop(self):
        self.pwm.stop()

