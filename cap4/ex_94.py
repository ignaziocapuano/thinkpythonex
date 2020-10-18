#i 3 lati possono formare un triangolo?

def checkTriangle(a,b,c):
    if (a<b+c and b<a+c and c<a+b):
        return True
    else:
        return False

def main():
    x=float(input("Inserisci primo lato: "))
    y=float(input("Inserisci secondo lato: "))
    z=float(input("Inserisci terzo lato: "))
    isTriangolo=checkTriangle(x,y,z)
    if isTriangolo:
        print("I 3 lati inseriti possono formare un triangolo")
    else:
        print("I 3 lati NON possono formare un triangolo")

main()