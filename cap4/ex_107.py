#riduzione frazione ai minimi termini

def massimoComuneDenominatore(a,b):
    mcd = min(a, b)  # massimo comune divisore

    while a % mcd != 0 or b % mcd != 0:
        mcd -= 1

def reduceFraction(n, d):
    if d==0:#se denominatore è 0
        print("Impossibile dividere per 0!")
        quit()

    if n==0: #se numeratore è 0
        return 0,1

    mcd = massimoComuneDenominatore(n,d)

    n=n//mcd #uso divisione intera per mantenere i valori interi enon farli diventare float
    d=d//mcd

    return n, d

def main():
    num=int(input("Inserisci numeratore:"))
    den=int(input("Inserisci denominatore:"))
    print("La frazione ridotta ai minimi termini è:",reduceFraction(num,den))

if __name__ == '__main__':
    main()

