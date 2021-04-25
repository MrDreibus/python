#Di cual es el numero mayor
num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

if num1 > num2:
	print("El numero " + str(num1) + " es mayor que " + str(num2));
elif num2 > num1:
	print("El numero " + str(num1) + " es menor que " + str(num2));
else:
	print("Los dos numeros son el " + str(num1));
