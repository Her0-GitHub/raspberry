import RPi.GPIO as GPIO
from time import sleep

# Scrivere pin con il "conteggio" fisico, pin 1 parte verso USB

#	rispettivamente
#      m1  m2  m3

EN  = [ 11, 8,  3]
IN1 = [ 13, 10, 5]
IN2 = [ 15, 12, 7]

def setup(): # Imposta tutti i pin come output
	GPIO.setmode(GPIO.BOARD) # pin fisici non gpio
	for i in EN:
		GPIO.setup(i,GPIO.OUT)
	for i in IN1:
		GPIO.setup(i,GPIO.OUT)
	for i in IN2:
		GPIO.setup(i,GPIO.OUT)
	global enPWM
	enPWM = [GPIO.PWM(EN[0], 50), GPIO.PWM(EN[1], 50), GPIO.PWM(EN[2], 50)]
	for i in enPWM:
		i.start(0)

def endProgram():
	print("gg goodbye lol ez")
	turn(1, 0, True)
	turn(2, 0, True)
	turn(3, 0, True)
	for i in enPWM:
		i.stop()
	GPIO.cleanup()

def turn(motor, speed, direction):
	if(speed < 0):
		speed = 0
	elif(speed > 100):
		speed = 100
	enPWM[motor - 1].ChangeDutyCycle(speed)
	GPIO.output(IN1[motor - 1], not direction)
	GPIO.output(IN2[motor - 1], direction)

def avanti(speed):
	print("Avanti di " + str(speed))
	turn(1, 0, True)
	turn(2, speed, True)
	turn(3, speed, False)

def indietro(speed):
	print("Indietro di " + str(speed))
	turn(1, speed, True)
	turn(2, speed, False)
	turn(3, speed, True)

def destra(speed):
	print("Destra di " + str(speed))
	turn(1, speed, False)
	turn(2, speed//2, True)
	turn(3, speed//2, True)

def sinitra(speed):
	print("Sinistra di " + str(speed))
	turn(1, speed, True)
	turn(2, speed//2, False)
	turn(3, speed//2, False)

def digonaleTopDx(speed):
	print("Diagonale top dx di " + str(speed))
	turn(1, speed, True)
	turn(2, speed, False)
	turn(3, 0, True)

def diagonaleTopSx(speed):
	print("Diagonale top sx di " + str(speed))
	turn(1, speed, False)
	turn(2, 0, True)
	turn(3, speed, True)

def diagonaleBotDx(speed):
	print("Diagonale bot dx di " + str(speed))
	turn(1, speed, False)
	turn(2, speed, )
	turn(3, speed, )

def diagonaleBotSx(speed):
	print("Diagonale bot sx di " + str(speed))
	turn(1, speed, )
	turn(2, speed, )
	turn(3, speed, )

def rotazioneDx(speed):
	print("ruota destra di " + str(speed))
	turn(1, speed, True)
	turn(2, speed, True)
	turn(3, speed, True)


def rotazioneSx(speed):
	print("ruota sinistra di " + str(speed))
	turn(1, speed, False)
	turn(2, speed, False)
	turn(3, speed, False)