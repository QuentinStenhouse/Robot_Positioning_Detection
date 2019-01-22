import serial
import time
import Adafruit_BBIO.GPIO as GPIO
import sensor

echo = "P9_14" #Sensor echo pin
trigger = "P9_12" #Sensor trigger pin

if __name__ == '__main__':
	port = serial.Serial("/dev/ttyO1", baudrate = 9600)
	SENSOR = sensor.sensor(echo, trigger)
	SENSOR.GPIO_setup()
	while True:
		receive = port.read().decode()
		if receive == "G":
			port.write(str.encode("F"))
			SENSOR.get_distance_minus(50)
			port.write(str.encode("S"))
			time.sleep(0.1)
			#Get the UWB position
			port.write(str.encode("L"))
			SENSOR.get_distance_plus(75)
			port.write(str.encode("S"))
			port.write(str.encode("F"))
			SENSOR.get_distance_plus(80)
			port.write(str.encode("S"))
			port.write(str.encode("X"))
		if receive == "D":
			port.write(str.encode("R"))
			SENSOR.get_distance_plus(75)
			port.write(str.encode("S"))
			port.write(str.encode("F"))
			port.write(str.encode("S"))
			port.write(str.encode("Y"))
		if receive == "M":
			port.write(str.encode("R"))
			SENSOR.get_distance_plus(75)
			port.write(str.encode("S"))
			#while pos.start() == saved:
			port.write(str.encode("F"))
			port.write(str.encode("S"))
			port.write(str.encode("l"))
