#Especifica si el numero es positivo, negativo o neutro

num = int(input("Escribe un numero: "))

if num > 0:
	print("El numero " + str(num) + " es positivo")
elif num < 0:
	print("El numero " + str(num) + " es negativo")
else:
	print("El numero es neutro")
