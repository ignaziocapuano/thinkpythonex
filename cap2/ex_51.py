#equazioni secondo grado

import math

a=int(input("Inserisci coefficiente a: "))
b=int(input("Inserisci coefficiente b: "))
c=int(input("Inserisci coefficiente c: "))

discriminante=b**2-4*a*c

if discriminante<0:
    print("L'equazione non ha radici reali")
elif discriminante==0:
    soluzione=-b/(2*a)
    print("La soluzione è una ed è",soluzione)
elif discriminante>0:
    x1=(-b+math.sqrt(discriminante))/2*a
    x2 = (-b - math.sqrt(discriminante)) / 2*a
    print("L'equazione ha due soluzioni, x1=",x1,"x2=",x2)