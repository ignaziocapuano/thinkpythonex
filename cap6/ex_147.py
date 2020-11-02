#Checking for Winning Bingo Card

from ex_146 import createBingoCard, displayBingoCard

def isBingoCardWinning(card):
    #Check riga ORIZZONTALE
    for i in range(5):
        count=0
        for key in card:
            if card[key][i]==0:
                count+=1
        if count==5:
            return True
    #Check riga VERTICALE
    for key in card:
        count = 0
        for i in range(5):
            if card[key][i] == 0:
                count += 1
        if count == 5:
            return True
    #Check riga Diagonale1
    i=0
    count = 0
    for key in card:
        if card[key][i] == 0:
            count += 1
        i+=1
    if count == 5:
            return True
    #Check riga diagonale opposta
    i = 4
    count = 0
    for key in card:
        if card[key][i] == 0:
            count += 1
        i -= 1
    if count == 5:
        return True


def main():
    card=createBingoCard()
    """
    TEST ORIZZONTALE
    for key in card:
        card[key][0] = 0
    """
    """
    TEST VERTICALE
    for key in card:
        for i in range(5):
            card[key][i]=0
        break
    """
    """
    TEST DIAGONALE1(\)
    i = 0
    for key in card:
        card[key][i]=0
        i+=1
    """
    """
    TEST DIAGONALE2 (/)
    i = 4
    for key in card:
        card[key][i] = 0
        i -= 1
    """
    displayBingoCard(card)
    print(isBingoCardWinning(card))

if __name__ == '__main__':
    main()