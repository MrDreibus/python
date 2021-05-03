#Calcular el valor de x, sabiendo que x=a+b*c+0.5-d*c^2

numa = int(input("Dime el valor de la letra a: "))
numb = int(input("Dime el valor de la letra b: "))
numc = int(input("Dime el valor de la letra c: "))
numd = int(input("Dime el valor de la letra d: "))

total = numa+(numb*numc)+0.5-(numd*(numc**2))

print ("El resultado es " + str(total))
