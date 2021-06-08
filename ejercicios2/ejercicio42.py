#Introducir cadena y un carater y decir cuantas veces esta el caracter

valid = True
cont = 0
letra = "j"
frase = input("Dime una frase o una palabra: ")

while valid == True:
	letra = input("Dime un caracter: ")
	if (len(letra) == 1):
		valid = False

for i in range (0, len(frase)):
	if (frase[i] == letra):
		cont += 1

print("La letra " + letra.upper() + " aparece " + str(cont) + " veces en la frase")
