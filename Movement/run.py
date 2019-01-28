import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep
import math,time
from threading import Timer

class run:

	#Initialization of the class run
	def __init__(self,MotorAIN1,MotorAIN2,MotorAEN,MotorBIN1,MotorBIN2,MotorBEN,p_w_m):
		self.Motorain1 = MotorAIN1
		self.Motorain2 = MotorAIN2
		self.Motoraen = MotorAEN
		self.Motorbin1 = MotorBIN1
		self.Motorbin2 = MotorBIN2
		self.Motorben = MotorBEN
		self.Pwm = p_w_m

	def GPIO_setup(self):
		GPIO.setup(self.Motorain1,GPIO.OUT)
		GPIO.setup(self.Motorain2,GPIO.OUT)
		GPIO.setup(self.Motoraen,GPIO.OUT)
		GPIO.setup(self.Motorbin1,GPIO.OUT)
		GPIO.setup(self.Motorbin2,GPIO.OUT)
		GPIO.setup(self.Motorben,GPIO.OUT)

	#Setup the pwm parameter that the user want to achieve
	def pwm_setup(self, pwm1, pwm2):
		PWM.set_duty_cycle(self.Motoraen, pwm1)
		PWM.set_duty_cycle(self.Motorben, pwm2)

	#Procedure that let the wheels go forward
	def forward(self):
		GPIO.output(self.Motorain1,GPIO.HIGH)
		GPIO.output(self.Motorain2,GPIO.LOW)
		PWM.start(self.Motoraen,30)
		GPIO.output(self.Motorbin1,GPIO.HIGH)
		GPIO.output(self.Motorbin2,GPIO.LOW)
		PWM.start(self.Motorben,30)
	#Procedure that let the wheels go backward
	def backward(self):
		GPIO.output(self.Motorain1,GPIO.LOW)
		GPIO.output(self.Motorain2,GPIO.HIGH)
		GPIO.output(self.Motoraen,GPIO.HIGH)
		GPIO.output(self.Motorbin1,GPIO.LOW)
		GPIO.output(self.Motorbin2,GPIO.HIGH)
		GPIO.output(self.Motorben,GPIO.HIGH)

	#Procedure which let the left wheel go backward
	def left_turn(self):
		GPIO.output(self.Motorbin1, GPIO.LOW)
		GPIO.output(self.Motorbin2, GPIO.HIGH)
		PWM.start(self.Motorben,70)

	#Procedure which let the right wheel go backward
	def right_turn(self):
		GPIO.output(self.Motorain1, GPIO.LOW)
		GPIO.output(self.Motorain2, GPIO.HIGH)
		PWM.start(self.Motoraen,70)

	#Procedure which stop both wheels
	def stop(self):
		PWM.stop(self.Motoraen)
		PWM.stop(self.Motorben)

	#Procedure which is used to avoid an obstacle
	def avoid_obstacle(self):
		self.stop()
		sleep(2)
		self.left_turn()
		sleep(1)
		self.stop()
		sleep(1)
		self.forward()
		sleep(2)
		self.stop()
		sleep(2)
		self.right_turn()
		sleep(1)
		self.stop()
		sleep(2)
		self.forward()

	#Those procedures are setting the parameters of the class run
	def setMotorAIN1(self,motorain1):
		self.Motorain1 = motorain1

	def setMotorAIN2(self,motorain2):
		self.Motorain2 = motorain2

	def setMotorAEN(self,motoraen):
		self.Motoraen = motoraien

	def setMotorBIN1(self,motorbin1):
		self.Motorbin1 = motorbin1

	def setMotorBIN2(self,motorbin2):
		self.Motorbin2 = motorbin2

	def setMotorBEN(self,motorben):
		self.Motorben = motorben

	def setPWM(self, pwm):
		self.Pwm = pwm
