#da ordinale a gregoriano

from ex_91 import checkBisestile
from ex_91 import ordinalDate

def ordinalToGregorianDate(y, d):
    bisestile=checkBisestile(y)
    ggNov=ggApr=ggGiu=ggSett=30
    ggGen=ggMar=ggMag=ggLug=ggAgo=ggOtt=ggDic=31
    if bisestile:
        ggFeb=29
        ggNoFeb=366-ggFeb
    else:
        ggFeb=28
        ggNoFeb=365-ggFeb
    giorno=d

    if d<ggGen:
        m=1

    if d>ggGen:
        m=2
        giorno-=ggGen

    if d>ggGen+ggFeb:
        m=3
        giorno-=ggFeb

    if d>ggGen+ggFeb+ggMar:
        m=4
        giorno-=ggMar

    if d>ggGen+ggFeb+ggMar+ggApr:
        m=5
        giorno-=ggApr

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag:
        m=6
        giorno-=ggMag

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu:
        m=7
        giorno-=ggGiu

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu+ggLug:
        m=8
        giorno-=ggLug

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu+ggLug+ggAgo:
        m=9
        giorno-=ggAgo

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu+ggLug+ggAgo+ggSett:
        m=10
        giorno-=ggSett

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu+ggLug+ggAgo+ggSett+ggOtt:
        m=11
        giorno-=ggOtt

    if d>ggGen+ggFeb+ggMar+ggApr+ggMag+ggGiu+ggLug+ggAgo+ggSett+ggOtt+ggNov:
        m=12
        giorno-=ggNov

    print("%2d" %giorno,"%2d"%m,y)

def testOrdinalToGregorian():
    anno=int(input("Inserisci anno: "))
    bisestile=checkBisestile(anno)
    giorno=int(input("Inserisci giorno dell'anno:"))
    while (giorno>366 and bisestile) or (giorno>365 and not bisestile):
        print("giorno non valido, inserisci giorno valido")
        giorno = int(input("Inserisci giorno dell'anno:"))
    ordinalToGregorianDate(anno,giorno)

def main():
    anno = int(input("Inserisci anno:"))
    mese = int(input("Inserisci mese in numero:"))
    giorno = int(input("Inserisci giorno"))
    intervallo= int(input("Inserire intervallo di giorni di cui visualizzare la data in giorni:"))

    dataSel=ordinalDate(anno, mese, giorno)
    dataFut= dataSel + intervallo
    bisestile=checkBisestile(anno)

    if (dataFut>366 and bisestile):
        dataFut-=366
    elif dataFut>365 and not bisestile:
        dataFut-=365
    anno+=1
    ordinalToGregorianDate(anno, dataFut)

main()
