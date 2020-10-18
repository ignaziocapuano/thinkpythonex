#Radice quadrata

"""
Algoritmo di Newton:
Leggi x
Ipotizza guess=x/2
WHILE guess non è sufficientemente buona DO
    update guess to be the average of guess and x/guess

Valutiamo la "bontà" con questo calcolo:
 se x-(guess^2)<=10^-12 allora è buona.

essendo guess la radice quadrata, facendo il quadrato dovremmo avvicinarci molto a x. quindi facciamo il metodo
fin quando l'errore assoluto non è nel range da noi deciso
"""

x=int(input("Inserisci numero di cui calcolare radice quadrata: "))

guess=x/2
print("Approssimazione:",guess)
errore=abs(x-guess**2)
print("Errore assoluto=",errore)


while errore>(10**(-12)):
    guess=(x/guess+guess)/2
    errore = abs(x - guess ** 2)
    print("Approssimazione:",guess)
    print("Errore assoluto=", errore)