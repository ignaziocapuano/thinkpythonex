#Reverse Lookups

def reverseLookup(dictionary,value):
    keys=[]
    for k in dictionary:
        #print(dictionary[k])
        if dictionary[k]==value:
            keys.append(k)
    return keys

def main():
    constants={"pi": 3.15,"g":9.8,"il senso della vita":42, "g2":9.8}
    print(constants)
    valore_da_trovare=float(input("Scegli valore da testare:"))
    print(reverseLookup(constants,valore_da_trovare))

if __name__ == '__main__':
    main()