#Palindromi con spazi e punteggiatura ignorati

"""
uso un ciclo loop per verificare che una parola sia palindroma.
Devo gestire 2 casi:
    parola di lettere pari
    parola di lettere dispari
Calcolo la posizione "specchio" di una lettera nella parola grazie alla funzione len()
nel caso di parole con lettere dispari ignorerò la posizione centrale
"""

parola=input("Inserisci una parola per verificare se sia un palindromo:")

lunghezza=len(parola)
startPos=0
endPos=lunghezza-1
"""
if lunghezza%2==0:
    pari=True
else:
    pari=False

In realtà non serve differenziare tra parole pari o dispari, andando a fare il for da
0 a lunghezza//2 arriveremo sempre alla lettera che ci serve, sia se la parola è pari sia se è dispari
"""
palindromo=True #LO SUPPONIAMO VERO, LO RENDIAMO FALSO QUANDO SCOPRIAMO CHE UNA LETTERA NON E SPECCHIATA
i=0

while(endPos-i>=1):
    """
    Dovendo ignorare spazi e punti, la condizione non può essere più come quella dell'es. precedente
    in cui bloccavo raggiunta la metà della parola, ma devo continuare finche le lettere che analizzo
    hanno al max 1 carattere in mezzo (nel caso di frasi con numero di caratteri dispari) o 0 se pari.
    """
    if (parola[i]).isalpha()==False: #Se il carattere della stringa non è una lettera dell'alfabeto ignorala e vai avanti.
        i+=1
    if (parola[endPos]).isalpha()==False: #Se il carattere della stringa non è una lettera dell'alfabeto ignorala e vai avanti.
        endPos-=1
    print(parola[i],"vs",parola[endPos]) #TEST
    if parola[i]!=parola[endPos]:
        palindromo=False
    endPos-=1
    i+=1

if palindromo:
    print("La parola è palindroma.")
else:
    print("La parola non è palindroma")
