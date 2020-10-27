#Evaluate Postfix

"""
Seguendo l'algoritmo descritto in traccia crea una funzione che risolva le espressioni in forma postfix
contenute in una lista ottenuta con le funzioni degli esercizi precedenti.
Notare che non è presente validazione dell'input quindi supponiamo l'inserimento sempre di espressioni corrette.
"""
from ex_129 import getTokens
from ex_130 import showUnaryTokens
from ex_131 import infixToPostfix

def evaluatePostfix(postfix_token_list):
    list_length=len(postfix_token_list)
    values=[]
    for i in range(list_length):
        if postfix_token_list[i].isnumeric():
            values.append(int(postfix_token_list[i]))
        elif postfix_token_list[i]=="u-":
            negative_value=values[len(values)-1]*(-1)
            values.pop()
            values.append(negative_value)
        elif postfix_token_list[i] in "+-*^/":
            operator=postfix_token_list[i]
            right=values[len(values)-1]
            values.pop()
            left=values[len(values)-1]
            values.pop()
            #print(left,"x",right)
            if operator=="+":
                result=left+right
            elif operator=="-":
                result=left-right
            elif operator=="*":
                result=left*right
            elif operator=="/":
                result=left/right
            elif operator=="^":
                result=left**right
            values.append(result)
        print("values=",values)
    return values[0]

def main():
    txt = input("Inserisci operazione matematica")
    tokens = getTokens(txt)
    #print(tokens)
    tokens_with_unary = showUnaryTokens(tokens)
    #print(tokens_with_unary)
    postfix_tokens=infixToPostfix(tokens_with_unary)
    #print(postfix_tokens)
    result=evaluatePostfix(postfix_tokens)
    print("Risultato=",result)

if __name__ == '__main__':
    main()

