#Only the Words

"""
Crea una funzione che estrae da una frase con punteggiatura tutte le parole, rimuovendo la punteggiatura da esse.
Non separare le parole in cui l'apostrofo è usato come forma contratta(in inglese)
"""

def getWords(string):
    parole=[]
    word=""
    #primo carattere
    if string[0] not in [" ", ".", "!", "?", ":", ";", "\n", ",","'"]:
            word += string[0]
    #caratteri intermedi
    for i in range(1,len(string)-1):
        if string[i] not in [" ",".","!","?",":",";","\n",","] or (string[i]=="'" and string[i+1] not in [" ",".","!","?",":",";","\n",","]):
                word+=string[i]
        else:
            if word!="":
                parole.append(word)
            word=""
    #ultimo carattere
    if string[len(string)-1] not in [" ", ".", "!", "?", ":", ";", "\n", ",", "'"]:
        word += string[len(string)-1]
    parole.append(word)
    return parole

def main():
    stringa=input("Inserisci una frase per estrarre le parole: ")
    print(getWords(stringa))


if __name__ == '__main__':
    main()
