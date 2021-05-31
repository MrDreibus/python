#Pedir un número por pantalla (un numero menor que 10) y visualizar por pantalla su tabla de multiplicar.
num = int(input("Dime de que numero quieres saber la tabla de multiplicar: "))


for i in range(0,11):
	print(str(num) + " x " + str(i) + " = " +str(num*i))
