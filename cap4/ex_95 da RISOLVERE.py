#Capitalize it - maiuscolizza

def sistemaMaiuscole(string):
    lunghezza=len(string)
    nuovaStr=string
    i=0
    while i<lunghezza and nuovaStr[i]==" ":
        i+=1
    if i<lunghezza:
        nuovaStr = nuovaStr[0:i]+nuovaStr[i].upper()+nuovaStr[i+1 : lunghezza]
    i=0
    while i<lunghezza:
        if nuovaStr[i]=="." or nuovaStr[i]=="!" or nuovaStr[i]=="?":
            i=i+1
            while i<lunghezza and nuovaStr[i]==" ":
                i=i+1

            if i<lunghezza:
                nuovaStr = nuovaStr[0:i]+nuovaStr[i].upper()+nuovaStr[i+1 : lunghezza]
        i=i+1
    i=1
    while i<lunghezza-1:
        if nuovaStr[i-1]==" " and nuovaStr[i]=="i" and (nuovaStr[i+1]==" " or nuovaStr[i+1]=="." or nuovaStr[i+1]=="!" or nuovaStr[i+1]=="?" or nuovaStr[i+1]=="'"):
            nuovaStr = nuovaStr[0:i]+nuovaStr[i].upper()+nuovaStr[i+1 : lunghezza]
            i+=1
    print(nuovaStr)


def main():
    stringa=input("Inserisci una stringa da sistemare: ")
    sistemaMaiuscole(stringa)

main()



