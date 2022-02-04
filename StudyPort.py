import random

#FUNCIONES 

def numPortService(numPor, nameService):
	solucion = input("Dime el nombre del servicio del puerto " + numPor + ": ")
	if (solucion.lower() == nameService.lower()):
		print("Correcto")

	elif (solucion == "exit"):
		print("Volviendo al menu")

	else:
		print("Incorrecto, el puerto es " + nameService)


	return solucion

def serviceNumPort(numPor, nameService):
	solucion = input("Dime el puerto servicio de " + nameService + ": ")
	if (solucion == numPor):
		print("Correcto")

	elif (solucion == "exit"):
		print("Volviendo al menu")
		
	else:
		print("Incorrecto, el puerto es " + numPor)

	return solucion

def menu():
	print ("=========Menu========")
	print ("1) De puerto a servicio")
	print ("2) De servicio a puerto ")
	print ("3) Salir")
	print ("=====================")


#PROGRAMA
puertos = ["20-21", "22", "23", "25-587", "53", "80", "110", "137-139", "143", "161-162", "443", "465", "514", "989-990", "993", "995", "3306", "3389", "1194"]
servicios =["FTP", "SSH", "Telnet", "SMTP", "DNS", "HTTP", "POP3", "NetBios", "IMAP", "SNMP", "HTTPs", "SMTPs", "syslog", "FTPs", "IMAP4s", "POP3s", "MySQL", "RPD", "OpenVPN"]

while True:
	menu()

	opc = int(input("Elige una opcion: "))
	cont = 0

	if opc == 1:
		print("Diga 'exit' para salir")

		while True:
			aleatorio = int(random.randint(0,len(puertos)-1))
			print(cont + 1)
			
			solucion = numPortService(puertos[aleatorio], servicios[aleatorio])
			cont += 1

			if (solucion == "exit"):
				break
		
	elif opc == 2:
		print("Diga 'exit' para salir")

		while True:
			aleatorio = int(random.randint(0,len(puertos)-1))
			print(cont + 1)
			
			solucion = serviceNumPort(puertos[aleatorio], servicios[aleatorio])
			cont += 1

			if (solucion == "exit"):
				break

	elif opc == 3:
		exit()
	else:
		print("Esta opcion no existe \nSaliendo...")
