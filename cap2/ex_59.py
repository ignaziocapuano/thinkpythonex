#data successiva

anno=int(input("Inserisci anno"))
mese=int(input("Inserisci mese in numero(valido)"))
giorno=int(input("Inserisci giorno(valido)"))

print("Hai digitato",anno,"/","%02d" % mese,"/","%02d" % giorno)

#CHECK BISESTILE
if anno%400==0:
    bisestile=True
else:
    #ANNI NON DIVISIBILI PER 400
    if anno%100==0:
        bisestile=False
    elif anno%4==0:
        bisestile=True
    else:
        bisestile=False

#CHECK CAMBIO MESE/ANNO

if mese==12 and giorno==31:
    anno+=1
    mese=1
    giorno=1
elif (mese==11 or mese==4 or mese==6 or mese==9) and giorno==30:
    mese+=1
    giorno=1
elif mese==2 and ((bisestile==False and giorno==28) or (bisestile==True and giorno==29)):
    mese+=1
    giorno=1
elif giorno==31:
    mese+=1
    giorno=1
else:
    giorno+=1

print("Il giorno successivo è",anno,"/","%02d" % mese,"/","%02d" % giorno)

