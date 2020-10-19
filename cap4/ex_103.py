#random good password

from ex_100 import generatePassword
from ex_102 import checkPassword

def main():
    password=generatePassword()
    tentativi=1
    while not checkPassword(password):
        password=generatePassword()
        tentativi+=1
    print("La password generata è:",password)
    print("Ci sono voluti",tentativi,"tentativi")

main()