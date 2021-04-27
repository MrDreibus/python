#Saca la nota sabiando que el 40% son los examens (2) y el 60% las practicas (4)

ex1 = int(input("Dime la nota del primer examen: "))
ex2 = int(input("Dime la nota del segundo examen: "))
p1 = int(input("Dime la nota de la primera practica: "))
p2 = int(input("Dime la nota de la segunda practica: "))
p3 = int(input("Dime la nota de la tercera practica: "))
p4 = int(input("Dime la nota de la cuarta practica: "))

notae = (((ex1 + ex2)/2)*40)/100
notap = (((p1 + p2 + p3 + p4)/4)*60)/100
print (notae)
notaf = notae + notap

print ("La nota final es : " + str(notaf))
