#negativi, 0, positivi

"""
inserita una lista di elementi interi dall'utente separa i negativi,gli 0 e i positivi in 3 liste diverse.
"""

from listInsertion import listInsertion

list=listInsertion("int","") #uso funzione creata in precedenza per inserire liste fino a inserimento carattere terminatore

negative_list=list.copy()
i=0
while i<len(negative_list):
    if negative_list[i]>=0:
        negative_list.remove(negative_list[i])
    else:
        i+=1
zero_list=list.copy()
i=0
while i<len(zero_list):
    if zero_list[i]!=0:
        zero_list.remove(zero_list[i])
    else:
        i+=1
positive_list=list.copy()
i=0
while i<len(positive_list):
    if positive_list[i]<=0:
        positive_list.remove(positive_list[i])
    else:
        i+=1

print(negative_list,zero_list,positive_list)

