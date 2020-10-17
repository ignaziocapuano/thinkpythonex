#bolletta telefonica

MAX_MINUTI=50
MAX_SMS=50
PREZZO_MENSILE_BASE=15.00
COSTO_MIN_EXTRA=0.25
COSTO_SMS_EXTRA=0.15
COSTO_ADDIZIONALE_911=0.44
PERCENTUALE_TASSE_TOT=5/100

minuti=int(input("Inserisci minuti di telefonate effettuati negli ultimi 30 giorni: "))
sms=int(input("Inserisci quantità SMS inviati negli ultimi 30 giorni: "))

if minuti>MAX_MINUTI or sms>MAX_SMS:
    tariffaExtra=True
    minExtra=minuti-MAX_MINUTI
    smsExtra=sms-MAX_SMS
else:
    tariffaExtra=False

if tariffaExtra==False:
    prezzoTot=PREZZO_MENSILE_BASE+COSTO_ADDIZIONALE_911
    print("SUBTotale          ", "%6.2f" % prezzoTot)
    tasse=prezzoTot*(PERCENTUALE_TASSE_TOT)
    prezzoTot=prezzoTot+tasse
    print("TARIFFA BASE         ","%6.2f" % PREZZO_MENSILE_BASE)
    print("COSTO ADDIZIONALE 911", "%6.2f" % COSTO_ADDIZIONALE_911)
    print("TASSA 5%             ", "%6.2f" % tasse)
    print("Totale               ", "%6.2f" % prezzoTot)
elif tariffaExtra==True:
    prezzoExtraMin=minExtra*COSTO_MIN_EXTRA
    if prezzoExtraMin<=0:
        prezzoExtraMin=0
        minExtra=0
    prezzoExtraSMS=smsExtra*COSTO_SMS_EXTRA
    if prezzoExtraSMS<=0:
        prezzoExtraSMS=0
        smsExtra=0
    prezzoTot = PREZZO_MENSILE_BASE + COSTO_ADDIZIONALE_911 + prezzoExtraMin + prezzoExtraSMS
    tasse = prezzoTot * (PERCENTUALE_TASSE_TOT)
    print("SUBTotale               ", "%6.2f" % prezzoTot)
    prezzoTot = prezzoTot + tasse
    print("TARIFFA BASE         ","%6.2f" % PREZZO_MENSILE_BASE)
    print("MINUTI EXTRA         ", "%6.2f" % prezzoExtraMin, "Minuti EXTRA","%3d" % minExtra, "(Costo/min)",COSTO_MIN_EXTRA)
    print("SMS EXTRA            ", "%6.2f" % prezzoExtraSMS, "SMS EXTRA   ","%3d" % smsExtra, "(Costo/sms)",COSTO_SMS_EXTRA)
    print("COSTO ADDIZIONALE 911", "%6.2f" % COSTO_ADDIZIONALE_911)
    print("TASSA 5%             ", "%6.2f" % tasse)
    print("Totale               ", "%6.2f" % prezzoTot)