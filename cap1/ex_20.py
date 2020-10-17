#gas ideali

import math

R_GASCONST=8.314

pressione=float(input("Inserisci pressione in Pascal:"))
volume=float(input("Inserisci volume in litri:"))
temperatura=float(input("Inserisci temperatura in Kelvin:"))

#PV=nRT
#moli=n

moli=(pressione*volume)/(R_GASCONST*temperatura)

print("Numero di moli: %.2f" % moli)


