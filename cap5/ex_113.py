#avoiding duplicates

"""
L'utente inserisce una serie di stringhe.
Finito il ciclo di inserimento (dopo aver inserito una stringa vuota) il programma restituisce la lista
delle stringhe inserite senza duplicati.
"""

list = []
str = input("Inserisci primo elemento della List: ")
while str != "":
    list.append(str)
    str = input("Inserisci numero da aggiungere alla List(0 per interrompere): ")

for i in range(0,len(list)-1):
    j=i+1
    while j<len(list):
        print(list[i],"vs",list[j])
        if list[j]==list[i]:
            list.pop(j)#SE l'elemento risulta uguale e lo rimuovo dovrò lasciare l'indice j uguale in quanto il pop ridurrà la dimensione della list
        else:
            j+=1

print(list)