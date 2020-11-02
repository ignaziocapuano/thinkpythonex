#Generate all sublists

def generateSublists(list):
    sublists=[]
    sub=[]
    sublists.append([])
    print(sublists)
    for i in range(0,len(list)):
        sub2=[]
        for k in range(i,len(list)):
            sub2.append(list[k])
            #print(sub2)
            sublists.append(sub2.copy()) #USO COPY perchè senza a quanto pare copia il puntatore e quindi non crea nuove liste a ogni ciclo.
            #print(sublists)
        sub2=[]
    return sublists

def main():
    list1 = []
    element = int(input("elemento="))
    while element != "":
        list1.append(int(element))
        element = input("Elemento(vuoto per terminare): ")
    print("La lista è ", list1)
    print("le sottoliste sono:",generateSublists(list1))

if __name__ == '__main__':
    main()