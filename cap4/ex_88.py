#mediana 3 valori

def mediana(a,b,c):
    if a<b<c:
        mediana=b
    elif c<b<a:
        mediana=b
    elif b<a<c:
        mediana=a
    elif c<a<a:
        mediana=a
    elif b<c<a:
        mediana=c
    elif a<c<b:
        mediana=c
    return mediana

def main():
    a=int(input("Inserisci valore a:"))
    b=int(input("Inserisci valore b:"))
    c=int(input("Inserisci valore c:"))
    print("La mediana è",mediana(a,b,c))

main()


