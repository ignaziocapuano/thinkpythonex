#da binario a decimale

bitString=input("Inserisci stringa binaria: ")

lunghezza=len(bitString)
numeroDecimale=0 #inizializzo

if bitString.count("1")+bitString.count("0")==lunghezza: #Stringa valida binaria
    esponente = lunghezza-1 #esponente per la conversione binario decimale
    for i in range(lunghezza):
        bit=int(bitString[i])*(2**esponente)
        numeroDecimale+=bit
        esponente-=1
    print(bitString, "In decimale corrisponde a ",numeroDecimale)
else:
    print("Non hai inserito un numero binario.")

