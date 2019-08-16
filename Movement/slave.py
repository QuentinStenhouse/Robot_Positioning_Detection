iimport serial
from time import sleep
import Adafruit_BBIO.GPIO as GPIO
import run

try:
	ser = serial.Serial(
	port = '/dev/ttyO1',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
	)
	Motor11 = "P8_9" # Input Pin 1
	Motor12 = "P8_11" # Input Pin 1
	Motor13 = "P8_19" # Enable Pin 1
	Motor21 = "P8_10" # Input Pin 2
	Motor22 = "P8_12" # Input Pin 2
	Motor23 = "P9_14" # Enable Pin 2
	ser.flushInput()
	ser.flushOutput()
	sleep(.1)
	print(ser.read(1))
	ser.write(str.encode("G"))
	RUN = run.run(Motor11,Motor12,Motor13,Motor21,Motor22,Motor23,100)
	RUN.GPIO_setup()
	while True:
		receive = ser.read(1)
		print(receive)
		if receive == b'F':
			RUN.forward()
		if receive == b'S':
			RUN.stop()
		if receive == b'L':
			RUN.left_turn()
		if receive == b'X':
			ser.flushOutput()
			sleep(.2)
			ser.write(str.encode("A"))
		if receive == b'R':
			RUN.right_turn()
		if receive == b'l':
			RUN.left_turn()
			sleep(10)
			RUN.stop()
			sleep(.1)
			RUN.forward()
			sleep(2)
			RUN.stop()
			ser.write(str.encode("G"))
		if receive == b'r':
			RUN.right_turn()
			sleep(10)
			RUN.stop()
			sleep(.1)
			RUN.forward()
			sleep(2)
			ser.write(str.encode("G"))
		if receive == b'T':
			RUN.left_turn()
			sleep(5)
			RUN.stop()

except KeyboardInterrupt:
	print("End")
GPIO.cleanup()
ser.close()
