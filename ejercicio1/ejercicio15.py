nombre = input("Dime su nombre: ")
apellido = input("Dime su apellido " + str(nombre) + " : ")
edad = int(input("Dime tu edad: "))

if (nombre == " " or apellido == " " or edad*0 != 0):
	print ("Hay un dato que no has introducido")

