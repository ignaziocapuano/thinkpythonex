#PREZZO DEL BIGLIETTO

"""
Ad uno zoo ci sono i seguenti prezzi
<2 anni gratis
3-12 anni 14%
65+ anni 18$
resto 23$
calcola quanto paga un gruppo di persone di età variegata sempre inserendo un valore alla volta fino
a che non viene inserita la linea vuota
"""

PREZZO_FASCIA0=0.0
PREZZO_YOUNG=14.00
PREZZO_ANZIANI=18.00
PREZZO_REGULAR=23.00


count=0
prezzoTot=0

line=input("Inserisci età del primo biglietto:")

while line!="":
    age=int(line)
    #CALCOLA PREZZO IN BASE A ETA
    if age <= 2:
        prezzoTot+=PREZZO_FASCIA0
    elif 3 <= age <= 12:
        prezzoTot+=PREZZO_YOUNG
    elif 13 <= age < 65:
        prezzoTot += PREZZO_REGULAR
    elif age >= 65:
        prezzoTot += PREZZO_ANZIANI
    count += 1  # incremento contatore
    line=input("Inserisci età del PROSSIMO biglietto(vuoto per terminare:")

print("Il prezzo totale è ","%.2f" % prezzoTot,"$ per",count, "biglietti")


