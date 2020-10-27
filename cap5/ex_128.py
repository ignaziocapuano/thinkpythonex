#Count the Elemens

def countRange(list, min_val, max_val):
    count=0
    for i in range(len(list)):
        if min_val<=list[i]<=max_val:
            print("list[",i,"]=",list[i])
            count+=1
    print(count)

def main():
    list = []
    element=float(input("Inserisci elemento:"))
    while element!="":
        list.append(float(element))
        element = input("Inserisci elemento( vuoto per terminare):")
    min=float(input("Inserisci soglia minima confronto: "))
    max=float(input("Inserisci soglia massima confronto: "))
    countRange(list,min,max)

if __name__ == '__main__':
    main()