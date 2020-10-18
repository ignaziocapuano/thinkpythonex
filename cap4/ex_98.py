#numeri primi

def isPrime(n):
    for i in range(2,n):#escludo 1 e se stesso perchè sempre divisibili e controllo che nessun numero di mezzo sia divisore
        #print(n,"%",i,"=",n%i)
        if n%i==0:
            return False
    return True

def main():
    n=int(input("Inserisci numero: "))
    if isPrime(n):
        print("è primo")
    else:
        print("non è primo")

if __name__ == '__main__':
    main()