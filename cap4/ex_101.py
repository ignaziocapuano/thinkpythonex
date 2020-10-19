#Codice patente casuale

"""
XXX000
0000XXX
equiprobabile tipo 1 o 2
"""

from random import randint

def generateLicense():
    lunghezza=randint(6,7)
    idPatente=""
    if lunghezza==6:
        for i in range(3):
            idPatente+=chr(randint(65,90)) #Le lettere maiuscole nella mappa ASCII vanno da 65 a 90
        for i in range(3):
            idPatente += str(randint(0, 9))
    elif lunghezza==7:
        for i in range(4):
            idPatente += str(randint(0, 9))
        for i in range(3):
            idPatente += chr(randint(65, 90))  # Le lettere maiuscole nella mappa ASCII vanno da 65 a 90
    return idPatente

def main():
    print("ID Patente generato=",generateLicense())

main()