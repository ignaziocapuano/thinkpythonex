#Da anno greogriano a ordinale (conta giorni)

def checkBisestile(y):
    # CHECK BISESTILE
    if y % 400 == 0:
        bisestile = True
    else:
        # ANNI NON DIVISIBILI PER 400
        if y % 100 == 0:
            bisestile = False
        elif y % 4 == 0:
            bisestile = True
        else:
            bisestile = False
    return bisestile

def ordinalDate(y, m, d):

    giornoDellAnno=d

    bisestile=checkBisestile(y)
    #CALCOLO GIORNO

    if m>11:
        giornoDellAnno+=30
    if m>10:
        giornoDellAnno+=31
    if m>9:
        giornoDellAnno+=30
    if m>8:
        giornoDellAnno+=31
    if m>7:
        giornoDellAnno+=31
    if m>6:
        giornoDellAnno+=30
    if m>5:
        giornoDellAnno+=31
    if m>4:
        giornoDellAnno+=30
    if m>3:
        giornoDellAnno+=31
    if m>2:
        if bisestile:
            giornoDellAnno+=29
        else:
            giornoDellAnno+=28
    if m>1:
        giornoDellAnno+=31

    return giornoDellAnno

def main():
    anno=int(input("Inserisci anno:"))
    mese=int(input("Inserisci mese in numero:"))
    giorno=int(input("Inserisci giorno"))
    print("Il giorno selezionato è il", ordinalDate(anno,mese,giorno),"esimo giorno del",anno)

if __name__ == '__main__':
    main()