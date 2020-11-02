#Roman Numerals

def romanNumberToInt(string):
    print("string=",string)
    char={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    if string== "":
        return 0
    if len(string)==1:
        return char[string]
    else:
        risultato=char[string[-1]]
        head=string[:-2]
        print(head)
        tail=string[-2:]
        if char[string[-2]]>=char[string[-1]]:
            return risultato+romanNumberToInt(head)
        else:
            return risultato-char[string[-2]]+romanNumberToInt(head)

def main():
    roman_number=input("Inserisci numero Romano: ")
    print("IN decimale è:", romanNumberToInt(roman_number))

main()

