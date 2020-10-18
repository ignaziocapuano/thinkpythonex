#CIFRATURA DI CESARE

"""
L'alfabeto usato da cesare è spostato di 3 caratteri. A -->D B-->E ecc.. X,Y,Z diventano A,B,C
caratteri non alfabetici non sono modificati dalla cifratura
Scrivi un programma che effettui uno shift seleziionabile su un messaggio inserito.
Uno shift negativo permette di decodificare i messaggi.
"""

messaggio=input("Inserisci Messaggio da Criptare con la cifratura di Cesare:")
shift=int(input("Inserisci lo shift dei caratteri(anche negativo): "))

LUNGHEZZA_ALFABETO=26

lunghezza=len(messaggio)

messaggiocriptato=""

for i in range(lunghezza):
    if messaggio[i].isalpha():
        pos=ord(messaggio[i])
        char=chr(pos)
        if "x"<=char<="z" or "X"<=char<="Z": #SE UNA DELLE ULTIME LETTERE VA TRASF. IN A/B/C, sottraggo quindi 26
            nwchr=chr(pos-LUNGHEZZA_ALFABETO +shift)
        else: #ALTRIMENTI faccio lo shift creando un carattere con posizione in ascii shiftata dello shift deciso
            nwchr = chr(pos + shift)
        messaggiocriptato+=nwchr
    else:
        messaggiocriptato+=messaggio[i]
print(messaggiocriptato)