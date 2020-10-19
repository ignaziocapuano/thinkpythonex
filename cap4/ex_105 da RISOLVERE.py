#conversioni arbitrarie

from ex_104 import hex2int
from ex_104 import int2hex

def bin2Dec(bitString):
    lunghezza = len(bitString)
    numeroDecimale = 0  # inizializzo
    if bitString.count("1") + bitString.count("0") == lunghezza:  # Stringa valida binaria
        esponente = lunghezza - 1  # esponente per la conversione binario decimale
        for i in range(lunghezza):
            bit = int(bitString[i]) * (2 ** esponente)
            numeroDecimale += bit
            esponente -= 1
        return numeroDecimale
    else:
        print("Non hai inserito un numero binario.")
        quit()

def dec2Bin(integer):
    if not integer.isnumeric():
        print("Non hai inserito un numero!")
        quit()
    bitString = ""
    while integer != 0:
        bit = integer % 2
        bitString = str(bit) + bitString
        integer = integer // 2
    return bitString

def baseToDecimal(num, base):
    if base
