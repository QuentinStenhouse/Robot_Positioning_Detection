# Robot_Positioning_Detection

This repository is made for the positioning of a robot, robot which must be able to detect obstacle and to avoid them.
The folder positioning contains for the moment the gerber files of a simple pcb with which you can use a DWM1000 module. The DWM1000 is radio frequencies component which use ultra wide band technology. This RF technology is able to return a distance and so it is used to position a robot in 2-D area. 

An other folder which is named detection is using the scripts that allow the robot to run in the 2-D and to detect obstacle with an ultrasonic sensor. Two beaglebone black are used and are communicating in UART. One is used for the detection and the positioning and the other one for the control of the motors. So the first one gives the instructions to the second one. 

