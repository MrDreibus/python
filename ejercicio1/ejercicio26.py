#Calcula el factorial de un numero
num = int(input("Dime un numero: "))
total = 1

for i in range (1, num+1, 1):
	total *= i
	print (str(i) + ".  " + str(total))

print ("El factorial de " + str(num) + " es : " + str(total))  
