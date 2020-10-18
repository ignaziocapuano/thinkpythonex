#la stringa è un intero?

def isInteger(str):
    x=str.lstrip()
    x=x.rstrip()
    if len(x)>1:
        if x[1]=="+" or x[1]=="-" or x[1].isnumeric():
            for i in range (1, len(x)):
                if not x[i].isnumeric():
                    return False
        else:
            return False
    elif len(x)==1:
        if x[0].isnumeric():
            return True
    else:
        return False
    return True

def main():
    num=input("inserisci numero per scoprire se è intero")
    if isInteger(num):
        print("è intero")
    else:
        print("non è intero")

main()