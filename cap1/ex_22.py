#areatriangolo
import math

lato1=float(input("Inserisci lato 1 in cm:"))
lato2=float(input("Inserisci lato 2 in cm:"))
lato3=float(input("Inserisci lato 3 in cm:"))

s=(lato1+lato2+lato3)/2

area=math.sqrt(s*(s-lato1)*(s-lato2)*(s-lato3))

print("Area del triangolo in cm^2: %.2f" % area)


