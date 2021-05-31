#Piedra papel o tijera
import random

i = 0
num = random.randint(1,3)

while i == 0: 

	print ("1. Piedra")
	print ("2. Papel")
	print ("3. Tijeras")

	opc = int(input("Dime una opcion: "))

	if (opc == 1):
		opcU = "Piedra"
		i = 1
	elif (opc == 2):
		opcU = "Papel"
		i = 1
	elif (opc == 3):
		opcU = "Tijeras"
		i = 1
	else:
		print ("No has elegido una opcion existente")

if (num == 1):
 	opcM = "Piedra"
elif (num == 2):
	opcM = "Papel"
elif (num == 3):
	opcM = "Tijeras"
               

print ("Maquina" + "\t\t" + "Usuario") 
print (opcM + "\t<-->\t" + opcU)

print ("..................")

if (opc == 1 and num == 1 or opc == 2 and num == 2 or opc == 3 and num == 3):
	print("Habeis quedado empate")
elif (opc == 1 and num == 3 or opc == 2 and num == 1 or opc == 3 and num == 2):
	print("Ha ganado el usuario")
else:
	print("Ha ganado la maquina")
