#Play Bingo

from ex_146 import createBingoCard, displayBingoCard
from ex_147 import isBingoCardWinning
from random import randint,shuffle

#Lo faccio all'italiana, pescando numeri in maniera casuale come a tombola
def playBingo():
    NUMERI_TOMBOLA=75

    card=createBingoCard()

    #displayBingoCard(card)
    numeri_disponibili=[]
    for i in range(76):
        numeri_disponibili.append(i)
    numeri_estratti=[]
    while len(numeri_disponibili)>0:
        indice_estratto=randint(0, len(numeri_disponibili) - 1)
        estratto=numeri_disponibili[indice_estratto]
        numeri_disponibili.pop(indice_estratto)
        numeri_estratti.append(estratto)
        #print("Estratto n=",i,"",estratto)
        for key in card:
            for i in range(5):
                if estratto==card[key][i]:
                    card[key][i]=0
        vincente=isBingoCardWinning(card)
        if vincente:
            break
    #print(numeri_estratti)
    #print(len(numeri_estratti))
    #displayBingoCard(card)
    return len(numeri_estratti)

def main():
    estrazioni_necessarie=[]
    for i in range(1000):
        estrazioni_necessarie.append(playBingo())
    min_estrazioni=min(estrazioni_necessarie)
    max_estrazioni=max(estrazioni_necessarie)
    avg_estrazioni=sum(estrazioni_necessarie)/1000
    print("Min Estrazioni per vincere=",min_estrazioni,"\nMax estrazioni per vincere:",max_estrazioni,"\nMedia estrazioni per vincere=",avg_estrazioni)

if __name__ == '__main__':
    main()



