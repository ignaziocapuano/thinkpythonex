#Congettura di Collatz

"""
Costruisci una sequenza in questo modo:
-Primo termine intero, unico nella sequenza
WHILe ultimo termine sequenza!=1
DO
SE L'ULTIMO TERMINE E' PARI
aggiungi termine facendo divisione intera dell'ultimo termine diviso 2
ALTRIMENTI
aggiungi termine moltiplicando *3 ultimo termine eaggiungendo 1
"""

n=int(input("Inserisci numero intero per ottenere la sequenza di Collatz:"))
print(n)

while n!=1:
    if n%2==0: #ultimo termine pari
        n=n//2
    else: #ultimo termine dispari
        n=n*3+1
    print(n)