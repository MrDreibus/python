#Simulacion del lanzamiento de una moneda el aire 20 veces

import random

for i in range (0, 20):
	num = random.randint(1,2)
	if (num == 1):
		print ("Cara")
	else:
		print ("Cruz")

