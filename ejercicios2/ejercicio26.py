#26)Realizar un código fuente que lea un importe por teclado y calcule el importe con un 10%
#de descuento y la cantidad que se le ha descontado.

importe = int(input("Dime el importe: "))
importet = importe-(importe*10)/100
descuento = importe - importet

print ("Se ha rabajado un 10%, el importe total es de " + str(importet) + " euros")
print ("Se te ha rebajado " + str(descuento) + " euros")

