nombre = input("Dime su nombre: ")
apellido = input("Dime su apellido " + str(nombre) + " : ")
edad = int(input("Dime tu edad: "))

if (nombre == "null" or apellido == "null" or edad == "null"):
	print ("Hay un dato que no has introducido")

