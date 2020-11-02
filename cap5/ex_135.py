#The sieve of eratosthenes

"""
Algoritmo per trovare i numeri primi tra 2 e un numero superiore  ascelta.
-Scrivi tutti i numeri da 0 a limit
-rimuovi 0 e 1 perchè non sono primi

p=2
while p<limit:
    togli tutti i multipli di p tranne p
    setta p al prossimo numero della lista che non è stato tolto

stampa tutti i numeri non rimossi.(sono quelli primi)

NON RIMUOVIAMO GLI ELEMENTI DALLA LISTA, ma settiamoli a 0, sarà più semplice gestire l'algoritmo e avrà
un costo computazionale minore. Alla fine creiamo una lista con tutti i valori diversi da 0 che saranno appunto
quelli sleezionati dall'algoritmo.
"""

def erathostenesPrimeNumbers(limit):
    list=[]
    for i in range(limit):
        list.append(i)
    list[0]=None
    list[1]=None
    p=2
    while p<limit:
        #CONSIDERA CHE p=list[p]
        #print("p=",list[p])
        for i in range(p+1,limit):
            if i%p==0:
                list[i]=None
        k=p+1
        while k<len(list)-1 and list[k]==None:
            k+=1
        p=k

    list2=[]
    for i in range(limit):
        if list[i]!=None:
            list2.append(list[i])
    return list2

def main():
    lim=int(input("Inserire estremo superiore per la ricerca dei numeri primi tra 2 e il valore scelto: "))
    print(erathostenesPrimeNumbers(lim))

if __name__ == '__main__':
    main()
