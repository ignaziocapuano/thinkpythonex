#nextPrime

from ex_98 import isPrime

def nextPrime(n):
    while not isPrime(n):
        n+=1
        isPrime(n)
    return n

def main():
    n=int(input("Inserisci numero per scoprire il succesivo numero primo"))
    print("Il succesivo numero primo è",nextPrime(n))

if __name__ == '__main__':
    main()