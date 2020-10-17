#areapoligono
import math

n_lati=int(input("Inserisci numero di lati:"))
l_lati=float(input("Inserisci lunghezza lato:"))

area=n_lati*l_lati**2/(4*math.tan(math.pi/n_lati))

print("Area del poligono di",n_lati,"lati: %.2f" % area)


