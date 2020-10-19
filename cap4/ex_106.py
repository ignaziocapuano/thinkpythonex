#giorni in un mese

def monthDays(y,m):
    if m<0 or m>12:
        print("mese inserito non valido")
        quit()
    #check bisestile
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
    #Check mese
    if (m==11 or m==4 or m==6 or m==9):
        days=30
    elif (m==2):
        if bisestile:
            days=29
        else:
            days=28
    else:
        days=31
    return days

def main():
    anno=int(input("Inserisci anno: "))
    mese=int(input("Inserisci mese: "))
    giorni=monthDays(anno,mese)
    print("Questo mese ha",giorni,"giorni")

main()