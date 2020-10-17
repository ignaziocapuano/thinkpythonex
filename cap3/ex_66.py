#no more pennies

"""
inserisci una serie di prezzi fin quando non inserisci un valore vuoto,
il totale viene arrotondato a multipli di 5 cent perchè non sono più prodotti i 1cent in canada
"""

prezzoTot=0

line=input("Inserisci prezzo articolo acquistato(vuoto per terminare): ")

while line!="":
    prezzoElemento=float(line)
    prezzoTot+=prezzoElemento
    line = input("Inserisci prezzo articolo acquistato(vuoto per terminare): ")

print("Prezzo totale non arrotondato: ",prezzoTot)

#arrotondamento
prezzoInPenny=prezzoTot*100
print("Prezzo in penny=",prezzoInPenny)
fattoreResto=prezzoInPenny%5
print("Fattor resto=",fattoreResto)

if fattoreResto<2.5:
    prezzoInPenny-=fattoreResto
else:
    prezzoInPenny=prezzoInPenny+(5-fattoreResto)
print("Prezzo arrotondato: %.2f" % (prezzoInPenny/100))
