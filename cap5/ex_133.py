#Does a List contain a Sublist?

def isSublist(larger,smaller):
    if len(smaller)==0 or smaller==larger: #Se la sublista è vuota o se è uguale alla lista
        return True
    elif len(smaller)==1 and smaller[0] in larger:
        return True
    elif len(smaller)>1:
        count=0
        for i in range(len(smaller)):
            for j in range(len(larger)):
                #print(smaller[i], "vs", larger[j])
                if smaller[i]==larger[j]:
                    #print(smaller[i], "=", larger[j])
                    count=1
                    delta=j-i #FACCIO IN MODO CHE I CICLI SCORRANO INSIEME
                    for k in range(i+1,len(smaller)):
                        #print("k=",k)
                        for n in range(k+delta,len(larger)):
                            #print("n=",n)
                            #print(smaller[k],"vs",larger[n])
                            if smaller[k]==larger[n]:
                                count+=1
                                #print(smaller[k], "=", larger[n])
                            else:
                                break
                    break
            break

        print("Elementi consecutivi della lista small uguali a elementi consecutivi della lista large=",count)
        if count==len(smaller):
            return True
        else:
            return False
    else:
        return False
def main():
    list1=[]
    element = int(input("elemento="))
    while element != "":
        list1.append(int(element))
        element = input("Elemento(vuoto per terminare): ")
    print("La lista grande è ",list1)
    print("Inserisci lista massimo grande quanto la principale:")
    list2=[]
    while len(list2)<len(list1) and True:
        element=input("Elemento(vuoto per terminare): ")
        if element=="":
            break
        else:
            list2.append(int(element))
    print("La lista piccola è ", list2)
    bool=isSublist(list1,list2)
    print(bool)

if __name__ == '__main__':
    main()