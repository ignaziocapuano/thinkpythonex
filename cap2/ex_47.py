#Segno zodiacale da mese e anno

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

if (meseNum==1 and data<=19) or (meseNum==12 and data>=22):
    segnoZodiacale= "Capricorno"
elif (meseNum==1 and data>=20) or (meseNum==2 and data<=18):
    segnoZodiacale= "Acquario"
elif (meseNum == 2 and data >= 19) or (meseNum == 3 and data <= 20):
    segnoZodiacale = "Pesci"
elif (meseNum == 3 and data >= 21) or (meseNum == 4 and data <= 19):
    segnoZodiacale = "Ariete"
elif (meseNum == 4 and data >= 20) or (meseNum == 5 and data <= 20):
    segnoZodiacale = "Toro"
elif (meseNum == 5 and data >= 21) or (meseNum == 6 and data <= 20):
    segnoZodiacale = "Gemelli"
elif (meseNum == 6 and data >= 21) or (meseNum == 7 and data <= 22) :
    segnoZodiacale = "Cancro"
elif (meseNum == 7 and data >= 23) or (meseNum == 8 and data <= 22) :
    segnoZodiacale = "Leone"
elif (meseNum == 8 and data >= 23) or (meseNum == 9 and data <= 22):
    segnoZodiacale = "Vergine"
elif (meseNum == 9 and data >= 23) or (meseNum == 10 and data <= 22):
    segnoZodiacale = "Bilancia"
elif (meseNum == 10 and data >= 23) or (meseNum == 11 and data <= 21):
    segnoZodiacale = "Scorpione"
elif (meseNum == 11 and data >= 22) or (meseNum == 12 and data <= 21):
    segnoZodiacale = "Sagittario"

print(segnoZodiacale)