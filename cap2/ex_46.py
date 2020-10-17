#Stagione da mese e anno

mese=input("Inserisci mese: ")
data=int(input("Inserisci data: "))

if mese=="Gennaio":
    meseNum=1
elif mese=="Febbraio":
    meseNum = 2
elif mese == "Marzo":
    meseNum = 3
elif mese == "Aprile":
    meseNum = 4
elif mese == "Maggio":
    meseNum = 5
elif mese == "Giugno":
    meseNum = 6
elif mese == "Luglio":
    meseNum = 7
elif mese == "Agosto":
    meseNum = 8
elif mese == "Settembre":
    meseNum = 9
elif mese == "Ottobre":
    meseNum = 10
elif mese == "Novembre":
    meseNum = 11
elif mese == "Dicembre":
    meseNum = 12

if (meseNum<=3 and data<20) or (meseNum==12 and data>=21):
    stagione="Inverno"
elif (meseNum==3 and data>=20) or (meseNum==6 and data<21) or(3<meseNum<6):
    stagione="Primavera"
elif (meseNum == 6 and data >= 21) or (meseNum == 9 and data < 22) or (6 < meseNum < 9):
    stagione = "Estate"
elif (meseNum == 9 and data >= 22) or (meseNum == 12 and data < 21) or (9 < meseNum < 12):
    stagione = "Autunno"

print(stagione)