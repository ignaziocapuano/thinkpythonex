#Pig Latin Improved

def pigTranslateWord(word):
    print("PAROLA=",word)
    vowels="AaEeIiOoUu"
    if word[0] in vowels:
        word+="way"
    else:
        if word[0].isupper():
            maiuscolo=True
            word=word.lower()
            word=word[1].upper()+word[2:]+word[0]+"ay"
        else:
            word = word[1] + word[2:] + word[0] + "ay"
    return word

def pigTranslateShift(word):
    vowels = "AaEeIiOoUu"
    if word[0] in vowels:
        return 3+1#se parola inizia con vocale la nuova parola sarà più lunga di 3 caratteri
    else:
        return 2+1#se inizia con consonante di 2


frase=input("Inserire frase da tradurre in Pig Latin: ")

lunghezza_frase=len(frase)

word=""

terminators=[" ", ".", "!", "?", ":", ";", "\n", ",", "'","+"]

if frase[0] not in terminators:
    word_start=0
    word+=frase[0]
    print("Word=", word)
# caratteri intermedi
i=1
while i<lunghezza_frase-1:
    if frase[i] not in terminators:#il carattere è una lettera
        if frase[i-1] not in terminators:#il carattere precedente è una lettera
            if frase[i + 1] not in terminators:#il carattere successivo è una lettera
                word += frase[i] #Siamo nel mezzo di una parola
                i+=1
                print("Word=",word)
            else:#siamo alla fine di una parola
                word_end=i
                word += frase[i]
                print("Word=", word)
                print("FINE PAROLA!")

                frase=frase[:word_start]+pigTranslateWord(word)+frase[word_end+1:]
                i+=pigTranslateShift(word)
                lunghezza_frase = len(frase) #aggiorno lunghezza frase
                word=""

        else:#siamo all'inizio di una parola
            word_start=i
            print("Word start=",frase[word_start])
            word+=frase[i]
            i+=1
    else:
        i+=1
    #Se si arriva qui stiamo analizzando un carattere terminatore
# ultimo carattere
if lunghezza_frase>1:
    if frase[lunghezza_frase - 1] not in terminators:
        if frase[lunghezza_frase -2] not in terminators:
            word_end=lunghezza_frase-1
            word+=frase[lunghezza_frase - 1]
            print("word end=", frase[word_end])
            print("Word=", word)
            frase = frase[:word_start] + pigTranslateWord(word) +frase[word_end+1:]
print(frase)

"""
Non è perfetta. probabilmente la traccia richiedeva di fare la traduzione
solo di una parola e non di una frase intera,al momento funziona bene tranne che per le parole singole in italiano
tipo le congiunzioni.
"""