#hex-decimal

"""
hex2int converte un singolo esadecimale
0 1 2 3 4 5 6 7 8 9 A B C D E F
int2hex converte un decimale tra 0 e 15
"""

def hex2int(hexDigit):
    #CONTROLLO CHE SIA UN SOLO CARATTERE
    if len(hexDigit)>1:
        print("La cifra inserita non è esadecimale!")
        quit() #TERMINA SE ERRORE
    #CONTROLLO CHE SIA UN NUMERO TRA 0 e 9
    if hexDigit.isnumeric() and 0<int(hexDigit)<9:
        return hexDigit
    else:#ADESSO VERIFICO SE E UNA LETTERA, CON I CASI PARTICOLARI. SE NON SARà NESSUNO DI QUESTI RITORNERà ERRORE IN CODA ALLA FUNZIONE.
        hexDigit=hexDigit.upper() #RENDO EVENTUALMENTE MAIUSCOLO
    if hexDigit=="A":
        return 10
    elif hexDigit=="B":
        return 11
    elif hexDigit=="C":
        return 12
    elif hexDigit=="D":
        return 13
    elif hexDigit=="E":
        return 14
    elif hexDigit=="D":
        return 15
    #Se nessuno dei casi precedenti, sarà un carattere sbagliato
    print("Non hai inserito un numero esadecimale.")
    quit()


def int2hex(intLimited):
    if (intLimited<0 or intLimited>15):
        print("Valore fuori dal range.")
        quit()
    if 0<intLimited<9:
        return intLimited
    elif intLimited==10:
        hexDigit="A"
    elif intLimited==11:
        hexDigit="B"
    elif intLimited==12:
        hexDigit="C"
    elif intLimited==13:
        hexDigit="D"
    elif intLimited==14:
        hexDigit="E"
    elif intLimited==15:
        hexDigit="F"
    return hexDigit

def main():
    hex=input("Inserisci cifra esadecimale:")
    print("In decimale è ",hex2int(hex))
    integer=int(input("Inserisci decimale tra 0 e 15:"))
    print("In esadecimale è ",int2hex(integer))

main()