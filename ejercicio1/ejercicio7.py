#Di cual es el mayor y el menor entre estos tres numeros
num1 = int(input("Dime el primer numero: "));
num2 = int(input("Dime el segundo numero: "));
num3 = int(input("Dime el tercer numero: "));

if num1 > num2 and num1 > num3:
	if num2 > num3:
		print ("El numero mayor es " + str(num1) + " y el numero menor es " + str(num3));
	else:
		print ("El numero mayor es " + str(num1) + " y el numero menor es " + str(num2));
elif num2 > num1 and num2 > num3:
	if num1 > num3:
		print ("El numero mayor es " + str(num2) + " y el numero menor es " + str(num3));
	else:
		print ("El numero mayor es " + str(num1) + " y el numero menor es " + str(num1));
else:
	if num1 > num2:
		print ("El numero mayor es " + str(num3) + " y el numero menor es " + str(num2));
	else:
		print ("El numero mayor es " + str(num3) + " y el numero menor es " + str(num1));
