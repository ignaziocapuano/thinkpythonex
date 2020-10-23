#rimuovi max e min

"""
Crea una funzione che acquisita una lista e un numero n>0 vada a copiare la lista rimuovendo gli n elementi più grandi e gli n elementi più piccoli.
"""

def removeOutliers(list,n):
    #Input Validation Check
    if n<1:
        print("Numero n troppo piccolo!")
        quit()
    if len(list)<4:
        print("Lista troppo piccola!")
        quit()
    #Funzione
    list.sort()
    for i in range(n):
        list.pop()
    for i in range(n):
        list.pop(0)
    return list

def main():
    list = []
    num = int(input("Inserisci primo elemento della List: "))
    while num != 0:
        list.append(num)
        num = int(input("Inserisci numero da aggiungere alla List(0 per interrompere): "))
    qt_outliers=int(input("Inserisci numero di elementi ai bordi da rimuovere:"))
    print(removeOutliers(list,qt_outliers))

main()
