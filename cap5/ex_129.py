#Tokenizing a String

"""
Separa una stringa in Tokens:
es in un operazione matematica i tokens sono numeri, operatori o parentesi.
La funzione restituisce la lista con i token.
"""
def getTokens(string):
    token_list=[]
    token=""
    numbers="1234567890"
    operators="+-*^/()[]{}"

    #primo carattere
    if string[0] in numbers:
        if len(string)>1:
            token += string[0]
            if string[1] not in numbers:
                token_list.append(token)
        else:
            token += string[0]
            token_list.append(token)
    elif string[0] in operators:
        token=string[0]
        token_list.append(token)
        token=""
    #caratteri intermedi
    for i in range(1,len(string)-1):
        if string[i] in numbers:
            if string[i+1] in numbers:
                token+=string[i]
            else:#token numerico terminato
                token+=string[i]
                token_list.append(token)
                token=""
        elif string[i] in operators:
            token=string[i]
            token_list.append(token)
            token=""
        else:
            token=""
    #ultimo carattere
    if len(string)>1:
        if string[len(string)-1] in numbers:
            token += string[len(string)-1]
            token_list.append(token)
        elif string[len(string)-1] in operators:
            token = string[len(string)-1]
            token_list.append(token)
    return token_list

def main():
    txt=input("Inserisci operazione matematica")
    print(getTokens(txt))

if __name__ == '__main__':
    main()
