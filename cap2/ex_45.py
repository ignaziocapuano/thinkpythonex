#scacchiera

casella=input("Inserire casella scacchiera tra a1 e h8:")


if casella[0]=="a" or casella[0]=="c" or casella[0]=="e" or casella[0]=="g":
    coloreNeroIniziale=True
else:
    coloreNeroIniziale=False

#riga=int(casella[1])

if int(casella[1])%2==0 and coloreNeroIniziale==True:
    colore="Bianco"
else:
    colore="Nero"

print("La casella ",casella,"è di colore", colore)