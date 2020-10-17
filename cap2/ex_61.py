#validità patente
"""
I codici vecchio stile sono in formato XXX000
I codici nuovo stile sono in formato 0000XXX"
"""

idPatente=input("Inserisci codice patente:")

lunghezzaID= len(idPatente)

if idPatente[0].isalpha() and idPatente[1].isalpha() and idPatente[2].isalpha() and idPatente[3].isnumeric() and idPatente[4].isnumeric() and idPatente[5].isnumeric():
    tipo="Vecchio stile"
elif idPatente[0].isnumeric() and idPatente[1].isnumeric() and idPatente[2].isnumeric() and idPatente[3].isnumeric() and idPatente[4].isalpha() and idPatente[5].isalpha() and idPatente[6].isalpha():
    tipo="Nuovo stile"
elif lunghezzaID<6 or lunghezzaID>7:
    tipo="Non valido"
else:
    tipo="Non valido"

print("Il codice patente inserito è",tipo)