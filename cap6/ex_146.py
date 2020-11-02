#Create a Bingo Card

"""
Tombola
"""
from random import randint

def createBingoCard():
    card={"B":[],"I":[],"N":[],"G":[],"O":[]}
    rangelow=1
    rangehi=15
    for key in card:
        count=0
        while count<5:
            casella=randint(rangelow,rangehi)
            if casella not in card[key]:
                card[key].append(casella)
                count+=1
                card[key]=sorted(card[key])
        rangelow+=15
        rangehi+=15
    return card

def displayBingoCard(card):
    print("B\tI\tN\tG\tO")
    for i in range(5):
        for key in card:
            print(card[key][i],end="\t")
        print("")

def main():
    card=createBingoCard()
    displayBingoCard(card)

if __name__ == '__main__':
    main()

