# Robot_Positioning_Detection

This repository is made for the positioning of a robot, robot which must be able to detect obstacle and to avoid them.




# The positioning folder

The folder positioning contains for the moment the gerber files of a simple pcb with which you can use a DWM1000 module. The DWM1000 is radio frequencies component which use ultra wide band technology. This RF technology is able to return a distance and so it is used to position a robot in 2-D area. We use the github link of ThingType which provides us a library in python of the DWM1000.




# The detection folder 

An other folder which is named detection (with an ultrasonic sensor) is using the scripts that allow the robot to run in the 2-D and to detect obstacle with an ultrasonic sensor. Two beaglebone black are used and are communicating in UART. One is used for the detection and the positioning and the other one for the control of the motors. So the first one gives the instructions to the second one. 

# The movement folder 

This folder contains the scripts to give commands to the motors with the beaglebone black.
