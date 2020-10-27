#Dealing Hands of Cards

from ex_125 import createDeck, shuffleDeck

def deal(num_giocatori, carte_mano, mazzo):
    mani=[]
    top_mazzo=len(mazzo)
    for i in range(num_giocatori):
        mani.append([""]*carte_mano)
    #Assembla mani
    for j in range(carte_mano):
        for i in range(num_giocatori):
            mani[i][j]=mazzo[len(mazzo)-1]
            mazzo.pop()

    for i in range(num_giocatori):
        print(mani[i])

    print(mazzo)
    print(len(mazzo))

def main():
    num_gioc=int(input("Inserisci numero giocatori:"))
    num_carte=int(input("Inserisci numero carte per mano:"))
    mazzo=createDeck()
    mazzo=shuffleDeck(mazzo)
    deal(num_gioc,num_carte,mazzo)

if __name__ == '__main__':
    main()

"""
Manca la validazione dell'input.
"""

