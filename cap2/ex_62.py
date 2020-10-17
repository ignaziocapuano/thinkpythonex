#ROULETTE
"""
La roulette ha 38 spazi
18 ner(2 4 6 8 10 11 13 15 17 20 22 24 26 28 29 31 35)
18 rossi(1 3 5 7 9 12 14 16 18 19 21 23 25 27 30 32 34 36)
2 verdi (0 e 00)

possibili giocate:
numero singolo
rosso/nero
pari/dispari (0 e 00 non sono pari)
1-18 19-36
"""

#ASSOCIO 00 all'intero -1, uso così la funzione randint di python tra -1 e 36

import random

ROSSI=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31,35]

numeroEstratto=random.randint(-1, 36)

print("Il numero estratto della roulette è:")

#SE non esce 0 o 00 aggiungi info
if numeroEstratto!=-1 and numeroEstratto>0:
    print(numeroEstratto)
    print("Paga", numeroEstratto)
    if numeroEstratto in ROSSI:
        print("Paga Rosso")
    else:#NERO
        print("Paga Nero")
    if numeroEstratto%2==0: #PARI
        print("Paga Pari")
    else:
        print("Paga Dispari")
    if numeroEstratto<19:
        print("Paga 1-18")
    else:
        print("Paga 19-36")
elif numeroEstratto==-1:
    print("00")
    print("Paga 00")
elif numeroEstratto==0:
    print("0")
    print("Paga 0")


