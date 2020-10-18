#perimetro poligono
"""
inserisci serie di punti tramite coordinate x,y e calcola poi il perimetro con i loop
quindi calcola la distanza tra ogni punto man mano che i punti vengono inseriti
"""

import math

perimetro=0.0

#INSERIMENTO PRIMO PUNTO

line=input("Inserisci coordinata X di partenza")
x0 = float(line)
line = input("Inserisci coordinata Y di partenza")
y0 = float(line)

#INIZIO LOOP INSERIMENTI

line = input("Inserisci coordinata X(vuoto per terminare)")

#CREO DUE VARIABILI CUSCINETTO, POICHE DEVO TENERE MEMORIZZATO IL PUNTO INIZIALE; MENTRE GLI ALTRI POSSO ANCHE DIMENTICARLI
#ANDANDO AVANTI NEL PROCEDIMENTO

x1=x0
y1=y0

while line!="":
    x = float(line)
    line = input("Inserisci coordinata Y")
    y = float(line)
    distanzaPunti=math.sqrt((x-x1)**2+(y-y1)**2) #Calcolo distanzaPunti
    perimetro+=distanzaPunti
    #Memorizzo in x1 e y1 le coordinate del punto precedente
    x1=x
    y1=y
    line = input("Inserisci coordinata X(vuoto per terminare)")

#CALCOLO ULTIMO LATO

distanzaPunti=math.sqrt((x1-x0)**2+(y1-y0)**2)
perimetro+=distanzaPunti

print("Il perimetro del poligono è",perimetro)
