#divisori propri

"""
Funzione che prende come parametro un intero e restituisce una lista dei suoi divisori.
"""

def properDivisors(num):
    divisors=[]
    for i in range(1,num//2+1):#Limito a n//2+1 per evitare cicli inutili da n/2+1 a n-1.
        if num%i==0:
            divisors.append(i)
    return divisors

def main():
    numero=int(input("Inserisci numero per ottenere i suoi divisori: "))
    print(properDivisors(numero))

if __name__ == '__main__':
    main()