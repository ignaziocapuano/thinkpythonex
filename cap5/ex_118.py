#Word by Word Palindromes

"""
Inserita una stringa, dire se la frase inserita è un palindromo parola per parola.
"""

from ex_117 import getWords

frase=input("Inserisci frase per scoprore se è palindroma: ")
frase=frase.lower()
parole=getWords(frase)
#print(parole)
endPos=len(parole)-1
palindromo=True
for i in range(0,len(parole)//2):
    #print(parole[i],"vs",parole[endPos]) #TEST
    if parole[i]!=parole[endPos]:
        palindromo=False
    endPos-=1


if palindromo:
    print("La parola è palindroma.")
else:
    print("La parola non è palindroma")