#caduta libera

import math

g=9.8

altezza=float(input("Inserisci altezza in m:"))

velocita_finale=(math.sqrt(2*g*altezza))

print("Velocità di impatto in m/s: %.2f" % velocita_finale)


