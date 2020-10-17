#cilindro

import math

raggio=float(input("Inserisci raggio in cm:"))
altezza=float(input("INserisci altezza in cm:"))

volume=((raggio**2)*math.pi)*altezza

print("Volume del cilindro in cm^2: %.1f" % volume)


