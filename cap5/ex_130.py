#Unary and Binary Operators

"""
Crea una funzione che, presa una lista di token(magari ottenuta con la funzione dell'esercizio precedente)
sostituisca agli operatori + e - la stringa "u+" o "u-" quando questi sono operatori unari(ovvero identificano il
segno del numero e non l'operazione di addizione e sottrazione)
es:
+3*-2+4 ---> Tokens: +, 3, *, -, 2, +, 4 -->f--->u+, 3, *, u-, 2, +, 4
"""

from ex_129 import getTokens



def showUnaryTokens(token_list):
    unaryoperators="+-"
    binaryoperators="*/^+-("
    for i in range(len(token_list)):
        if 0<i<len(token_list):
            if token_list[i] in unaryoperators:
                if token_list[i-1] in binaryoperators:
                    token_list[i]="u"+token_list[i]
        elif i==0:
            if token_list[i] in unaryoperators:
                token_list[i]="u"+token_list[i]
    return token_list

def main():
    txt = input("Inserisci operazione matematica")
    tokens=getTokens(txt)
    print(tokens)
    print(showUnaryTokens(tokens))

if __name__ == '__main__':
    main()
