#Capitalize it - maiuscolizza

def sistemaMaiuscole(string):
    lunghezza=len(string)
    nuovaStr=string
    for i in range(0,lunghezza):
        if i>=0 and string[i-1]==" ":
            nuovaStr = string[0:i]+string[i].upper()+string[i+1:lunghezza]
        #if string[i]=="." or string[i]=="!" or string[i]="?":
        #    while (string[j]==" " or string[j])
    print(nuovaStr)

def main():
    stringa=input("Inserisci una stringa da sistemare: ")
    sistemaMaiuscole(stringa)

main()



