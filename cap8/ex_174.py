#Massimo Comune Divisore

def massimoComuneDivisore(a,b):
    if b==0:
        return a
    else:
        c=a%b
        return massimoComuneDivisore(b,c)

def main():
    a = int(input("Inserisci primo numero: "))
    b = int(input("Inserisci secondo numero: "))
    print(massimoComuneDivisore(a,b))

if __name__ == '__main__':
    main()