#Lancio moneta

import random

N_SIMULAZIONI=10
N_OCCORRENZE_CONSECUTIVE=3

simulazioni=0
sommaLanci=0

while simulazioni<=N_SIMULAZIONI:
    flip=random.randint(0,1)
    countTesta=0
    countCroce=0
    countFlip=1
    lastflip=flip

    while countCroce<N_OCCORRENZE_CONSECUTIVE and countTesta<N_OCCORRENZE_CONSECUTIVE:
        if flip==0: #TESTA
            print("H", end=" ")
            if flip==lastflip:
                countTesta+=1
            else:
                countTesta=1
            #print("CountTesta=",countTesta)
        else: #CROCE
            print("T",end=" ")
            if flip==lastflip:
                countCroce+=1
            else:
                countCroce=1
            #print("CountCroce=", countCroce)
        lastflip = flip
        flip = random.randint(0, 1)
        countFlip+=1
    print("(",countFlip,"lanci)")
    simulazioni+=1 #NUOVA SIMULAZIONE
    sommaLanci+=countFlip

mediaLanci=sommaLanci/N_SIMULAZIONI
print("In media, sono serviti", mediaLanci," lanci.")


