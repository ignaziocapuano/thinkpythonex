#tabella sconti

PERCENTUALE_SCONTO=60/100
PREZZO_MIN_OGGETTO=4.95
PREZZO_MAX_OGGETTO=24.95
N_PREZZI_DIVERSI=5
"""
I PREZZI DEGLI OGGETTI RIENTRANO TRA QUESTI: 4,95 9,95 14,95 19,95 24,95. La differenza tra ogni prezzo è di 5.
Iteriamo quindi partendo dal prezzo più basso, e aggiungendo 5$ a ogni iterazione
DOVRO FARE 5 iterazioni, per cui l'argomento di range è 5 cioè N_PREZZI DIVERSI
potevo anche fare range(0,N_PREZZI DIVERSI,1) o (0,N_PREZZI_DIVERSI)
"""

prezzo=PREZZO_MIN_OGGETTO
differenziale=5

for i in range(N_PREZZI_DIVERSI):
    prezzoScontato=prezzo*PERCENTUALE_SCONTO
    print("PREZZO ORIGINALE $",prezzo,"PREZZO SCONTATO $=",round(prezzoScontato, 2))
    prezzo+=differenziale
