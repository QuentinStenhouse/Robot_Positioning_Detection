import Adafruit_BBIO.GPIO as GPIO
from threading import Timer
from time import sleep
import time

class sensor:

	#Initialisation of the class sensor
	def __init__(self,ECHO, TRIGGER):
		self.echo = ECHO
		self.trigger =TRIGGER

	def GPIO_setup(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.trigger, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)

	#Procedure which will get the distance of an obstacle
	def get_distance(self):
		GPIO.setup(self.trigger, GPIO.OUT)
		GPIO.setup(self.echo, GPIO.IN)
		pulse_start = 0
		pulse_end = 0
		GPIO.output(self.trigger, GPIO.HIGH)
		sleep(0.00001)
		GPIO.output(self.trigger, GPIO.LOW)
		while GPIO.input(self.echo) == 0:
			pulse_start = time.time()
		while GPIO.input(self.echo) == 1:
			pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start
		dist = pulse_duration*17150
		self.distan = round(dist, 2)
		GPIO.setup(self.echo, GPIO.OUT)
		GPIO.output(self.echo, GPIO.HIGH)
		sleep(0.00001)
		GPIO.setup(self.echo, GPIO.IN)
	def get_distance_plus(self, value):
                pulse_start = 0
                pulse_end = 0
                while True:
                        GPIO.output(self.trigger, GPIO.HIGH)
                        sleep(0.0001)
                        GPIO.output(self.trigger, GPIO.LOW)
                        while GPIO.input(self.echo) == 0:
                                pulse_start = time.time()
                        while GPIO.input(self.echo) == 1:
                                pulse_end = time.time()
                        pulse_duration = pulse_end - pulse_start
                        dist = pulse_duration*17150
                        self.distan = round(dist, 2)
                        GPIO.setup(self.echo, GPIO.OUT)
                        GPIO.output(self.echo, GPIO.HIGH)
                        sleep(0.00001)
                        GPIO.setup(self.echo, GPIO.IN)
                        if self.distan >= value:
                                return 1
	#Those procedures will set the parameters of the classe sensor
	def setEcho(self,Echo):
		self.echo = Echo

	def setTrigger(self,Trigger):
		self.trigger = Trigger

