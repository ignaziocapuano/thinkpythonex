#Infix to Postfix

"""
Le espressioni matematiche sono sempre nella forma "infix", in cui gli operatori compaiono tra gli operandi sui quali agiscono:
3+2
La forma "postfix" mette l'operatore dopo gli operandi:
3,2,+
L'algoritmo di conversione è nella traccia dell'esercizio.
Usiamo le funzioni degli esercizi 129 e 130 per tokenizzare un espressione e identificare gli operatori unari.
Usiamo poi l'algoritmo descritto nella traccia per trasformare le espressioni da infix a postfix.
"""

from ex_129 import getTokens
from ex_130 import showUnaryTokens

def precedence(op):
    if op=="+"  or op=="-":
        return 1
    elif op=="*" or op=="/":
        return 2
    elif op=="u+" or op=="u-":#COME DA TRACCIA
        return 3
    elif op=="^":
        return 4
    else:
        return -1

def infixToPostfix(infix_token_list):
    operatorslist=["+","-","*","/","^","u+","u-"]
    operators=[]
    postfix=[]
    for i in range(len(infix_token_list)):
        #print("[]=",infix_token_list[i])

        if infix_token_list[i].isnumeric():
            postfix.append(infix_token_list[i])
        elif infix_token_list[i] in operatorslist:
            while len(operators)>0 and operators[len(operators)-1]!="(" and precedence(infix_token_list[i])<precedence(operators[len(operators)-1]):
                postfix.append(operators[len(operators)-1])
                operators.pop()
            operators.append(infix_token_list[i])
        elif infix_token_list[i]=="(":
            operators.append(infix_token_list[i])
        elif infix_token_list[i]==")":
            while operators[len(operators)-1]!="(":
                postfix.append(operators[len(operators) - 1])
                operators.pop()
            operators.pop()
        #print("operatores=", operators)
        #print("postfix=", postfix)

    while len(operators)>0:
        postfix.append(operators[len(operators) - 1])
        operators.pop()
    return postfix

def main():
    txt = input("Inserisci operazione matematica")
    tokens = getTokens(txt)
    print(tokens)
    tokens_with_unary=showUnaryTokens(tokens)
    print(tokens_with_unary)
    print(infixToPostfix(tokens_with_unary))

if __name__ == '__main__':
    main()



