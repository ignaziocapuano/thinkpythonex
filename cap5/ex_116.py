#Perfect Numbers

"""
Un numero intero n è "Perfetto" quando la somma dei divisori propri di n è uguale a n.
Es: 28 ha come divisori 1 2 4 7 e 14, la cui somma fa 28
Scrivere una funzione che determina se un numero intero è perfetto o no.
Scrivere un main che mostri i numeri perfetti tra 1 e 10000.
Usa la funzione dell'esercizio precedente.
"""

from ex_115 import properDivisors

def isIntegerPerfect(integer):
    divisors=properDivisors(integer)
    sommaDivisors=0
    for i in range(len(divisors)):
        sommaDivisors+=divisors[i]
    if sommaDivisors==integer:
        #il numero è perfetto
        return True
    else:
        return False

def main():
    for i in range(1,10000):
        if isIntegerPerfect(i):
            print(i)

main()


