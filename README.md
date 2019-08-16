# Robot_Positioning_Detection

This repository is made for the positioning of a robot, robot which must be able to detect obstacle and to avoid them.
The robot must be able to localize himself in a 2D plan. We use 3 anchors with DWM1000 devices controlled by 3 Raspberry Pis 3 b+. Those anchors will returned the distance between them and a tag (the robot). When the robot has received all distances, the robot calculate his position in the 2D plan by doing a trilateration.   
The robot can avoid obstacle if it detects one with ultrasonic sensors. When the robot is at the end of the 2D plan, a turn around is done. Those scripts will evolve in the future.


# The positioning folder

The folder positioning contains for the moment the gerber files of a simple pcb with which you can use a DWM1000 module. The DWM1000 is radio frequencies component which use ultra wide band technology. This RF technology is able to return a distance and so it is used to position a robot in 2-D area. We use the github link of ThingType which provides us a library in python of the DWM1000 (https://github.com/ThingType/DW1000_Python_library). At this moment, the github link og ThingType doesn't work anymore, don't know why. This is why all the files you need are included in the different folders. This library is used for a "Raspberry PI". If like me you are using a "Beaglebone Black" make sure to change the gpio library in the DW1000 and to change the pins for the slave select and the irq in the different files. py file, to put on comment the line GPIO.setmode(GPIO.BCM). Last thing to know but not the least one, if you are loading the spi overlay at boot i do not know why but the "Slave Select" gives some problems. In my case the DWM1000 was not giving anything with the "Slave Select", so you just have to use an other "GPIO" like the pin "P9_15".


# The detection folder 

An other folder which is named detection (with an ultrasonic sensor) is using the scripts that allow the robot to run in the 2-D and to detect obstacle with an ultrasonic sensor. Two beaglebone black are used and are communicating in UART. One is used for the detection and the positioning and the other one for the control of the motors. So the first one gives the instructions to the second one. 

# The movement folder 

This folder contains the scripts to give commands to the motors with the beaglebone black. We use a "PID control" with the position in the XY which is given by the DWM1000 devices. 
