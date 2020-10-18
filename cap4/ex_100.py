#password casuale

from random import randint

def generatePassword():
    lunghezza=randint(7,10)
    password=""
    for i in range(lunghezza):
        password+=chr(randint(33,126))
    return password

def main():
    print("Password generata:",generatePassword())

if __name__ == '__main__':
    main()