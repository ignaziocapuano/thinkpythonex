#Below and Above Average

from listInsertion import listInsertion

lista=listInsertion("int","") #uso funzione creata precedentemente
somma_elementi=0
n_elementi=len(lista)
for i in range(len(lista)):
    somma_elementi+=lista[i]
media=somma_elementi/n_elementi
print("Media=",media)
lista_under=[]
for i in range(0,len(lista)):
    if lista[i]<media:
        lista_under.append(lista[i])
lista_avg=[]
for i in range(0,len(lista)):
    if lista[i]==media:
        lista_avg.append(lista[i])
lista_above=[]
for i in range(0,len(lista)):
    if lista[i]>media:
        lista_above.append(lista[i])
print("Valori sotto la media:",lista_under)
print("Valori pari alla media:",lista_avg)
print("Valori sopra la media:",lista_above)




