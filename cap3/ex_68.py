#MEDIA DEI VOTI inseriti a lettere

"""
Sfrutta l'es 52 per avere le conversioni. Al solito inserisci una serie di valori fin quando non si inserisce
una linea vuota e calcola la media dei valori man mano.
"""

media=0
count=0
sommaVoti=0

line=input("Inserisci voto in lettere (da A+ a F)")

while line!="":
    voto=line
    #CALCOLA VOTO IN NUMERI
    if voto== "A":
        votoNum=4.0
    elif voto== "A+":
        votoNum = 4.0
    elif voto == "A-":
        votoNum = 3.7
    elif voto == "B+":
        votoNum = 3.3
    elif voto == "B":
        votoNum = 3.0
    elif voto == "B-":
        votoNum = 2.7
    elif voto == "C+":
        votoNum = 2.3
    elif voto == "C":
        votoNum = 2.0
    elif voto == "C-":
        votoNum = 1.7
    elif voto == "D+":
        votoNum = 1.3
    elif voto == "D":
        votoNum = 1.0
    elif voto == "F":
        votoNum = 0
    count += 1  # incremento contatore
    sommaVoti+=votoNum
    media=sommaVoti/count
    line = input("Inserisci voto in lettere (da A+ a F)(vuoto per interrompere)")

print("La media dei voti digitati è ",media,"su",count, "valori inseriti")


