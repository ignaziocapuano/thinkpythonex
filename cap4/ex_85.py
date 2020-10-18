#ipotenusa

import math

def calcoloIpotenusa(a,b):
    ipotenusa=math.sqrt(a*2+b*2)
    return ipotenusa

def main():
    c1=float(input("Inserisci primo cateto"))
    c2=float(input("Inserisci secondo cateto"))
    c3=calcoloIpotenusa(c1,c2)
    print("l'ipotenusa è lungo", c3)

main()