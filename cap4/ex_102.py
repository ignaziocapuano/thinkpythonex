#password check

"""
almeno 8 caratteri
almeno 1 carattere maiuscolo
almeno 1 minuscolo
almeno 1 numero
"""

def checkPassword(pwd):
    if len(pwd)<8:
        return False
    else:
        countMaiusc=0
        countMinusc=0
        countDigit=0
        for i in range(len(pwd)):
            if pwd[i].isupper():
                countMaiusc+=1
            elif pwd[i].islower():
                countMinusc+=1
            elif pwd[i].isdigit():
                countDigit+=1
        if countMaiusc>0 and countMinusc>0 and countDigit>0:
            return True
        else:
            return False

def main():
    password=input("Inserisci password di almeno 8 caratteri con almeno 1 carattere maiuscolo, 1 minuscolo e un numero:")
    if checkPassword(password):
        print("Password valida")
    else:
        print("NON VALIDA")

if __name__ == '__main__':
    main()
