#Calculadora con funciones
#Funciones
def suma (num1 , num2):
	return num1 + num2
def resta (num1, num2):
	return num1 - num2
def multi (num1, num2):
	return num1 * num2
def div (num1, num2):
	if (num2 <= 0):
		return "No se puede dividir por 0"
	else:
		return num1 / num2

#-----------------------------------------------------
#Main
num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

print ("Suma --> " + str(suma(num1, num2)))
print ("Resta --> " + str(resta(num1, num2)))
print ("Multiplicar --> " + str(multi(num1, num2)))
print ("Dividir --> " + str(div(num1, num2)))

