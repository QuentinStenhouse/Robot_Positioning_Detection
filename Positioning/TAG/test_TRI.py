import math
import sys

def trilateration(r1,r2,r3,U1,V1,W1):
	global x,y
	ra = float(r1)
	rb = float(r2)
	rc = float(r3)
	U = float(U1)
	V = float(V1)
	W = float(W1)
	T = float(V**2 + W**2)

	if (U > ra + rb) and (W > ra + rc):
		print("No intersection, circles are too far apart")
	elif U > ra + rb:
		if W < abs(rc - ra):
			print("There is a circle inside the other one")
		else:
			y = float((ra**2 - rc**2 + W**2)/(2*W))
			x = float(math.sqrt(ra**2 - y**2 ))
			print("Cible en abscisse:",x)
			print("Cible en ordonée:",y)
	elif W > ra + rc:
		if U < abs(rb - ra):
			print("There is a circle inside the other one")
		else:
			x = float((ra**2-rb**2+U**2)/(2*U))
			y = float(math.sqrt(ra**2 - x**2 ))
			print("Cible en abscisse:",x)
			print("Cible en ordonée:",y)
	else:
		x = float(ra**2 - rb**2 + U**2)/float(2*U)
		y = float((ra**2 - rc**2+T-2*V*x)/float(2*W))
		print("Cible en abscisse:",x)
		print("Cible en ordonée:",y)
