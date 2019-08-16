import serial
import time
import Adafruit_BBIO.GPIO as GPIO
import sensor
import Self_Localization
import test_Tri

ser = serial.Serial(
   port = '/dev/ttyO1',
   baudrate = 9600,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS,
   timeout = 1
)
try:

	echo = "P9_14"
	trigger = "P9_12"
	echoG = "P9_29"
	triggerG = "P9_30"
	echoD = "P9_42"
	triggerD = "P9_41"
	PIN_IRQ = "P8_7"
	PIN_SS = "P9_15"
	Self_Localization.DW1000.begin(PIN_IRQ)
	Self_Localization.DW1000.setup(PIN_SS)
	Self_Localization.DW1000.generalConfiguration("82:17:5B:D5:A9:9A:E2:9C", Self_Localization.C.MODE_LONGDATA_RANGE_ACCURACY)
	Self_Localization.DW1000.registerCallback("handleSent",Self_Localization.handleSent)
	Self_Localization.DW1000.registerCallback("handleReceived", Self_Localization.handleReceived)
	Self_Localization.DW1000.setAntennaDelay(Self_Localization.C.ANTENNA_DELAY_RASPI)
	ser.flushInput()
	ser.flushOutput()
	SENSOR = sensor.sensor(echo, trigger)
	SENSOR.GPIO_setup()
	SENSORG = sensor.sensor(echoG, triggerG)
	SENSORG.GPIO_setup()
	SENSORD = sensor.sensor(echoD, triggerD)
	SENSORD.GPIO_setup()
	dist = float(100)
	y_minus_end = float(0)
	y_plus_end = float(3.37)
	while True:
		receive = ser.read(1)
		if receive == b'G':
			Self_Localization.DW1000Launch()
			r1 = Self_Localization.d1
			r2 = Self_Localization.d2
			r3 = Self_Localization.d3
			test_Tri.trilateration(r1, r2, r3, 2.18, 0, 3.14)
			ser.write(str.encode("F"))
			y = float(test_Tri.y)
			while float(-0.5 + y_plus_end) >= float(y) >= float(0.1 + y_minus_end):
				Self_Localization.DW1000Launch()
				r1 = Self_Localization.d1
				r2 = Self_Localization.d2
				r3 = Self_Localization.d3
				test_Tri.trilateration(r1, r2, r3, 2.18, 0, 3.14)
				y = float(test_Tri.y)
				SENSOR.get_distance()
				dist = float(SENSOR.distan)
				print(dist)
				if dist <= float(27):
					ser.write(str.encode("S"))
					x_mem = float(test_Tri.x)
					time.sleep(1)
					ser.write(str.encode("X"))
			if float(y) <= float(0.6 + y_minus_end):
				ser.write(str.encode("S"))
				time.sleep(1)
				ser.write(str.encode("l"))
			if float(y) >= float(-0.6 + y_plus_end):
				ser.write(str.encode("S"))
				time.sleep(1)
				ser.write(str.encode("r"))

		if receive == b'A':
			dist = float(0)
			time.sleep(1)
			ser.flushOutput()
			time.sleep(.1)
			while dist <= float(45):
				ser.write(str.encode("L"))
				SENSOR.get_distance()
				dist = float(SENSOR.distan)
				time.sleep(.2)
			dist = float(100)
			while dist >= float(30):
				ser.write(str.encode("L"))
				SENSORD.get_distance()
				dist = float(SENSORD.distan)
			dist = float(0)
			ser.flushOutput()
			ser.write(str.encode("S"))
			time.sleep(1)
			Self_Localization.DW1000Launch()
			r1 = Self_Localization.d1
			r2 = Self_Localization.d2
			r3 = Self_Localization.d3
			test_Tri.trilateration(r1, r2, r3, 2.25, 0, 3.37)
			x_mem = float(test_Tri.x)
			while x <= x_mem:
				while dist <= float(15):
					ser.write(str.encode("F"))
					time.sleep(.1)
					SENSORD.get_distance()
					dist =  float(SENSORD.distan)
					ser.flushOutput()
					time.sleep(.1)
				dist = float(100)
				ser.write(str.encode("S"))
				time.sleep(1)
				ser.flushOutput()
				time.sleep(.1)
				dist = float(100)
				while float(25) <= dist:
					ser.write(str.encode("R"))
					SENSORD.get_distance()
					dist = float(SENSORD.distan)
					time.sleep(.1)
				ser.flushOutput()
				ser.write(str.encode("S"))
				dist = float(0)
				time.sleep(1)
				Self_Localization.DW1000Launch()
				r1 = Self_Localization.d1
				r2 = Self_Localization.d2
				r3 = Self_Localization.d3
				test_Tri.trilateration(r1, r2, r3, 2.25, 0, 3.37)
				x = float(test_Tri.x)
			ser.flushOutput()
			time.sleep(.2)
			ser.write(str.encode("T"))
except KeyboardInterrupt:
	print("End")
GPIO.cleanup()
ser.close()
