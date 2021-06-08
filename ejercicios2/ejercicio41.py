#Muestra cada caracter de una frase o palabra

frase = input("Dime una frase o palabra: ")
long = len(frase)

for i in range (0, long):
	print(frase[i])

print("---> FIN")

