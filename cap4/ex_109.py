#date magiche

"""
quelle date in cui il prodotto tra giorno e mese è uguale alle ultime due cifre dell'anno.
scrivi funzione che dica se una data è magica
e un main che mostra tutte le date magiche del 20esimo secolo
"""

from ex_106 import monthDays

def isMagicDate(y,m,d):
    #estrapola ultime due cifre dell'anno
    anno=str(y)
    cifreAnno=len(anno)
    annoXX=anno[cifreAnno-2]+anno[cifreAnno-1]
    annoXX=int(annoXX)
    #check magic date
    if d*m==annoXX:
        return True
    else:
        return False

def main():
    for anno in range(1900,2000):
        for mese in range(1,12):
            giorniMese=monthDays(anno, mese)
            for giorno in range(1,giorniMese):
                if isMagicDate(anno,mese,giorno):
                    print("%02d" % giorno,"/","%02d" % mese,"/",anno)

main()