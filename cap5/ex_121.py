#Random Lottery Numbers

from random import randint

numeri_estratti=[]
#prima estrazione
estratto=randint(1,49)
numeri_estratti.append(estratto)
#successive estrazioni
for i in range(5):
    while estratto in numeri_estratti:
        estratto=randint(1,49)
    numeri_estratti.append(estratto)
print(sorted(numeri_estratti))
