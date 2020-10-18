#cerca massimo tra 100 elementi randomici interi

import random

N_ELEMENTI=100
n=random.randint(1,100)
print(n)
max=n
count=0 #conta aggiornamenti di massimo

for i in range(1,N_ELEMENTI):#creo altri 99 numeri
    n=random.randint(1,100)
    print(n,end="")
    if n>max:
        max=n
        count+=1
        print(end="\t<==Update")
    print()#a capo

print("Valore massimo=",max)
print("il valore max è stato aggiornato", count,"volte")