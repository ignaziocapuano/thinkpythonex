#Punteggio scrabble

letter_value={"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"R":1,"S":1,"T":1,"U":1,"D":2,"G":2,\
              "B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}

parola=input("Inserisci parola di cui calcolare punteggio: ").upper()
punteggio=0
#print(letter_value.keys())
#for i in range(len(parola)):
    #print(parola[i])
    #if parola[i] in letter_value.keys():
     #   punteggio+=letter_value[parola[i]]
for ch in parola:
    #print(ch)
    if ch in letter_value.keys():
        punteggio+=letter_value[ch]
print("Punteggio=",punteggio)