import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

IN1 = 17
IN2 = 18
ENA = 22

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

pwm = GPIO.PWM(ENA, 100)
pwm.start(0)

GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

pwm.ChangeDutyCycle(100)

time.sleep(10)

pwm.stop()
GPIO.cleanup()
