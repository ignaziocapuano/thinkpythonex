#Shuffling deck of cards

"""
52 carte
4 semi spades,hearts,diamonds,clubs
2-10 jack queen king ace
Rappresenta carta con valore in maiuscolo e seme in minuscolo
"""
from random import randint

def createDeck():
    deck=[]
    for i in range(2,11):#Spades
        deck.append(str(i)+"s")
    deck.append("Js")
    deck.append("Qs")
    deck.append("Ks")
    deck.append("As")
    for i in range(2,11):#Hearts
        deck.append(str(i)+"h")
    deck.append("Jh")
    deck.append("Qh")
    deck.append("Kh")
    deck.append("Ah")
    for i in range(2,11):#Diamonds
        deck.append(str(i)+"d")
    deck.append("Jd")
    deck.append("Qd")
    deck.append("Kd")
    deck.append("Ad")
    for i in range(2,11):#Clubs
        deck.append(str(i)+"c")
    deck.append("Jc")
    deck.append("Qc")
    deck.append("Kc")
    deck.append("Ac")
    return deck

def shuffleDeck(deck):
    #unbiased algorithm: scambio un elemento con uno a caso tra i successivi
    for i in range(51):#il mazzo ha 52 carte(con l'algoritmo scelto lavorare sull'ultima carta non ha senso)
        pos=randint(i,51)
        temp=deck[pos]
        deck[pos]=deck[i]
        deck[i]=temp
    return deck

def main():
    mazzo=createDeck()
    print(mazzo)
    mazzo=shuffleDeck(mazzo)
    print(mazzo)

if __name__ == '__main__':
    main()