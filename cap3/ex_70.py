#bit di parità

line=input("Inserisci stringa binaria di 8 bit")

"""
Come posso controllare che la stringa inserita sia binaria?
innanzitutto controllo la lunghezza di 8 bit, poi uso il metodo count per contare le occorrenze di 1 e 0 nella stringa e
mi assicuro che siano esattamente 8
"""

while line!="":
    #Controllo stringa
    if (line.count("0")+line.count("1") != 8 ) or len(line)!=8:
        print("Non hai inserito una stringa di 8 bit.")
    else:
        bitUno=line.count("1")
        #PARITA'
        if bitUno%2==0:
            print("Il bit di parità sarà 0 perche ci sono",bitUno," bit 1 nella stringa")
        else:
            print("Il bit di parità sarà 1 perche ci sono", bitUno," bit 1 nella stringa")
    line = input("Inserisci stringa binaria di 8 bit")