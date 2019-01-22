import serial
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import run
from ivPID import PID
import cons

Motor11 ="P8_9" # Input Pin 1
Motor12 = "P8_11" # Input Pin 1
Motor13 = "P8_19" # Enable Pin 1
Motor21 = "P8_12" # Input Pin 2
Motor22 ="P8_10" # Input Pin 2
Motor23 = "P9_14" # Enable Pin 2
detector1 = "P8_15" #Encoder Pin 1
detector2 = "P8_16" #Encoder Pin 2

if __name__ == '__main__':
	port = serial.Serial("/dev/ttyO1", baudrate = 9600)
	port.write(str.encode("G"))
	RUN = run.run(Motor11,Motor12,Motor13,Motor21,Motor22,Motor23,100)
	RUN.GPIO_setup()
	period = 600/(float(23)*70)
	P1 = 0.1
	I1 = 0
	D1 = 0
	P2 = 0.1
	I2 = 0
	D2 = 0
	pid1 = PID.PID(P1, I1, D1)
	pid1.setSampleTime(period)
	pid2 = PID.PID(P2, I2, D2)
	pid2.setSampleTime(period)
	CONS = cons.cons(period,70,detector1,detector2)
	CONS.GPIO_setup()
	CONS.init_interrupt1()
	CONS.init_interrupt2()
	while True:
		receive = port.read().decode()
		print(receive)
		if receive == "F":
			RUN.forward()
			response = ""
			while response != "S":
				CONS.cons_value()
				pid1.SetPoint = CONS.cons_1
				pid1.update(CONS.val_cons1)
				pid2.SetPoint = CONS.cons_2
				pid2.update(CONS.val_cons2)
				CONS.PWM_out(pid1.output,pid2.output)
				pwm1_output = 70 + CONS.pwm1
				pwm2_output = 70 + CONS.pwm2
				RUN.pwm_setup(pwm1_output,pwm2_output)
				CONS.pulse_reset()
				sleep(period)
				response = port.read().decode()
		if response == "S":
			RUN.stop()
		if receive == "L":
			RUN.left_turn()
		if receive == "X":
			CONS.pulse_reset()
			while CONS.pulse1 < 42:
				RUN.forward()
			RUN.stop()
			port.write(str.encode("D"))
		if receive == "R":
			RUN.right_turn()
		if receive == "l":
			CONS.pulse_reset()
			while CONS.pulse1 <32:
				RUN.left_turn()
			RUN.stop()
		if receive == "r":
			CONS.pulse_reset()
			while CONS.pulse2 <32:
				RUN.right_turn()
			RUN.stop()
		if receive == "T":
			CONS.pulse_reset()
			while CONS.pulse1 <64:
				RUN.left_turn()
			RUN.stop()
		if receive == "Y":
			CONS.pulse_reset()
			while CONS.pulse1 < 42:
				RUN.forward()
			RUN.stop()
			port.write(str.encode("M"))
