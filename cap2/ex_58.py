#anni bisestili

anno=int(input("Inserisci ANNO:"))

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

if bisestile==True:
    print("L'anno digitato è bisestile")
else:
    print("L'anno digitato non è bisestile")
