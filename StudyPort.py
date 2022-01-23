
import random

#FUNCIONES 

def numPortService(numPor, nameService):
	solucion = input("Dime el nombre del servicio del puerto " + numPor + ": ")
	if (solucion.lower() == nameService.lower()):
		print("Correcto")
	else:
		print("Incorrecto, el puerto es " + nameService)

def serviceNumPort(numPor, nameService):
	solucion = input("Dime el puerto servicio de " + nameService + ": ")
	if (solucion == numPor):
		print("Correcto")
	else:
		print("Incorrecto, el puerto es " + numPor)

def menu():
	print ("=========Menu========")
	print ("1) De puerto a servicio")
	print ("2) De servicio a puerto ")
	print ("3) Salir")
	print ("=====================")


#PROGRAMA
puertos = ["20-21", "22", "23", "25-587", "53", "80", "110", "137-139", "143", "161-162", "443", "465", "514", "989-990", "993", "995", "3306", "3389", "1194"]
servicios =["FTP", "SSH", "Telnet", "SMTP", "DNS", "HTTP", "POP3", "NetBios", "IMAP", "SNMP", "HTTPs", "SMTPs", "syslog", "FTPs", "IMAP4s", "POP3s", "MySQL", "RPD", "OpenVPN"]

menu()

opc = int(input("Elige una opcion: "))

if opc == 1:
	for i in range (0,10,1):

		aleatorio = int(random.randint(0,len(puertos)-1))
		print(i+1)
		
		numPortService(puertos[aleatorio], servicios[aleatorio])
	
elif opc == 2:
	for i in range (0,10,1):

		aleatorio = int(random.randint(0,len(puertos)-1))
		print(i+1)
		
		serviceNumPort(puertos[aleatorio], servicios[aleatorio])
elif opc == 3:
	exit()
else:
	print("Esta opcion no existe \nSaliendo...")
