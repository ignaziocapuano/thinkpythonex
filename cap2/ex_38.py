#Mese-->numero di giorni

mese=input("Inserisci un mese:")

if mese== "novembre" or mese== "aprile" or mese== "giugno" or mese== "settembre":
    print("30 giorni")
elif mese== "febbraio":
    print("28 giorni")
elif mese== "gennaio" or mese== "marzo" or mese== "maggio" or mese== "luglio" or mese== "agosto" or mese== "ottobre"or mese== "dicembre":
    print("31 giorni")
else:
    print("non è un mese")