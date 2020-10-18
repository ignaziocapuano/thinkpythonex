#Tabelline

"""
usa l'argomento end="" alla funzione print per stampare senza andare a capo
"""

#STAMPA CORNICE GRAFICA
print(end="\t")
for i in range(1,10+1):
    print(i, end="\t")
print("")

for i in range(1,10+1):
    print(i, end="\t")#STAMPA L'INDICE DI RIGA
    for j in range(1, 10+1):
        print(i*j, end="\t")
    print()