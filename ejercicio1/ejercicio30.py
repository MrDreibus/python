#numero aleatorio del 1 al 10 y salga si se equivoca 3 veces

import random
import math
numf = math.trunc(random.random()*20)
cont = 0

while True:
	num = int(input("Dime un numero: "))

	if (num > numf):
		print ("El numero es menor")
		cont+=1
	elif (num < numf):
		print ("El numero es mayor")
		cont+=1
	else:
		print ("Bieeen, lo has acertado")
		break

	if (cont == 3):
		break
	
	print(cont)
