#Pig Latin

"""
Se una parola inizia con vocale, "way" è aggiunto alla fine della parola.
Se inizia con consonante, le lettere della parola fino alla prima vocale sono tolte e aggiunte alla fine della parola aggiungendo "ay".
Es:
computer->omputercay
office->officeway
"""

from ex_117 import getWords

frase=input("Inserisci frase da tradurre in pig english: ")
parole=getWords(frase)
n_parole=len(parole)
for i in range(n_parole):
    word=parole[i]
    if word[0] in ["a","e","i","o","u"]:
        word+="way"
    else:
        new_word=""
        for j in range(1,len(word)):
            new_word+=word[j]
        new_word+=word[0]+"ay"
        word=new_word
    parole[i]=word
frase_tradotta=""
for i in range(n_parole):
    frase_tradotta+=parole[i]+" "
print(frase_tradotta)