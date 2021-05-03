#Mostrar resultado de la suma de los numeros , desde el que se introduce hasta el 0
num = int(input("Dime un numero: "))
suma = 0

for i in range (num, 0, -1):
	suma+=i

print("El resultado de la suma es: " + str(suma))
