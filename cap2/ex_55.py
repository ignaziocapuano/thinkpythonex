#lunghezza d'onda luce


lunghezzaOnda=float(input("Inserisci lunghezza d'onda tra 380 e 750:"))

valido=True

if 380 <= lunghezzaOnda < 450:
    colore= "Violetto"
elif 450 <= lunghezzaOnda < 495:
    colore= "Blue"
elif 495 <= lunghezzaOnda < 570:
    colore= "Verde"
elif 570 <= lunghezzaOnda < 590:
    colore= "Giallo"
elif 590 <= lunghezzaOnda < 620:
    colore= "Arancio"
elif 620 <= lunghezzaOnda < 750:
    colore= "Rosso"
else:
    valido=False

if valido==False:
    print("Valore non valido")
else:
    print("Il colore è: ", colore)