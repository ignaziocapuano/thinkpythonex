#Recursive Decimal to Binary

def decimalToBinaryRecursive(decimal):
    if decimal<0:
        print("Valore non valido")
        quit()
    if decimal==0:
        return "0"
    elif decimal==1:
        return "1"
    else:
        next_digit = decimal % 2
        risultato = decimalToBinaryRecursive(decimal//2) +str(next_digit)

    return risultato

def main():
    decimal_int=int(input("Inserisci numero non negativo da convertire in binario:"))
    print(decimalToBinaryRecursive(decimal_int))

if __name__ == '__main__':
    main()