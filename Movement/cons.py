import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC
from time import sleep
import math,time
from threading import Timer

#Class cons which is used to calculate the pulse from the wheels and calculate the value of the pwm that the two encoders see
class cons:

	#Init the class cons
	def __init__(self, per, p_w_m, enc1, enc2):
		self.Period = per
		self.Pwm = p_w_m
		self.detector1 = enc1
		self.detector2 = enc2
		self.pulse1 = 0
		self.pulse2 = 0

	def GPIO_setup(self):
		GPIO.setup(self.detector1,GPIO.IN)
		GPIO.setup(self.detector2,GPIO.IN)

	#Initialisation of the interruption from encoder 1 and encoder 2 wheels
	def init_interrupt1(self):
		GPIO.add_event_detect(self.detector1, GPIO.RISING,self.PulseA, bouncetime = 1)

	def init_interrupt2(self):
		GPIO.add_event_detect(self.detector2, GPIO.RISING,self.PulseB, bouncetime = 1)

	def PulseA(self, PULSE1):
		self.pulse1 += 1

	def PulseB(self, PULSE2):
		self.pulse2 += 1

	def cons_value(self):
		self.cons_1 = (float(self.Pwm)*2.3) #Get the PWM that the user want to achieve
		self.cons_2 = (float(self.Pwm)*2.3) #Get the PWM that the user want to achieve
		pulse_per_tour = 20 #Number of pulse that the encoders can see per tour
		freq_encoder1 = float(self.pulse1)/self.Period #Frequency of the pulse of wheel 1
		tour_per_sec1 = float(freq_encoder1) / pulse_per_tour #Tours per seconde of wheel 1
		self.val_cons1 = (float(tour_per_sec1)*60) #Tours per minute of wheel 1
		freq_encoder2 = float(self.pulse2)/self.Period #Same as whheel 1 but for wheel 2
		tour_per_sec2 = float(freq_encoder2) / pulse_per_tour
		self.val_cons2 = (float(tour_per_sec2)*60)

	def pulse_reset(self):
		self.pulse1 = 0
		self.pulse2 = 0

	def PWM_out(self, PWM1, PWM2):
		self.pwm1 = float(PWM1)/2.3
		self.pwm2 = float(PWM2)/2.3
	#Set manually a value of a parameter of the class cons
	def setPeriod(self, period):
		self.Period = period

	def setPWM(self, pwm):
		self.Pwm = pwm

	def setenc1(self, detect1):
		self.detector1 = detect1

	def setenc2(self, detect2):
		self.detector2 = detect2
