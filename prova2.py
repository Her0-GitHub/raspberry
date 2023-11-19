import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# motore 1 / 2 / 3
IN1 = [10, 17, 14]
IN2 = [ 9, 27, 18]
ENA = [11, 22, 15]

GPIO.cleanup()

for i in range(3):
    GPIO.setup(IN1[i], GPIO.OUT)
    GPIO.setup(IN2[i], GPIO.OUT)
    GPIO.setup(ENA[i], GPIO.OUT)

pwm = [GPIO.PWM(ENA[0], 100),GPIO.PWM(ENA[1], 100),GPIO.PWM(ENA[2], 100)]

for i in range(3):
    pwm[i].start(0)
    pwm[i].ChangeDutyCycle(100)

    GPIO.output(IN1[i], GPIO.HIGH)
    GPIO.output(IN2[i], GPIO.LOW)

def avanti():
    print("avanti")
    GPIO.output(IN1[2], GPIO.HIGH)
    GPIO.output(IN2[2], GPIO.LOW)
    GPIO.output(ENA[2], GPIO.LOW)

def indietro():
    print("indietro")

while True:
    match(input("Inserisci mossa: ")):
        case 'w':
            avanti()
        case 's':
            indietro()
        case 'x':
            pwm[0].stop()
            pwm[1].stop()
            pwm[2].stop()
            GPIO.cleanup()
            exit()
    #time.sleep(10)


