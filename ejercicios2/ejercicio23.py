#Cuantos numeros se introducen hasta introducir el 0
cont = 0
while True:
	num = int(input("Dime un numero: "))
	if (num == 0):
		break
	else:
		cont+=1
print ("Se han introducido " + str(cont) + " numeros")
