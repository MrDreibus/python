#Se quiere diseñar el algoritmo de un programa que pida por teclado la nota (dato real) de
#una asignatura y muestre por pantalla su equivalente en palabra.

num = int(input("Dime la nota total de la asignatura: "))

if (num == 10 or num == 9):
	print("Sobresaliente")
if (num == 8 or num == 7):
	print("Notable")
if (num == 6):
	print ("Bien")
if (num == 5):
	print("suficiente")
if (num < 5):
	print("Insuficiente")
