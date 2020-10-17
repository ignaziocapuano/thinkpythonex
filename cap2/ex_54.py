#Votazione impiegati

votoNum=float(input("Inserisci voto dell'impiegato in punteggio tra 0.0 0.4 o >=0.6 :"))

valido=True

if votoNum>=0.6:
    valutazione= "Performance Meritevole"
elif votoNum==0.4:
    valutazione= "Performance Accettabile"
elif votoNum==0.0:
    valutazione= "Performance Inaccettabile"
else:
    valido=False

if valido==False:
    print("Voto non valido")
else:
    aumento=votoNum*24000
    print("L'impiegato ha ottenuto una ", valutazione,"e per cui avrà un aumento di $",aumento )