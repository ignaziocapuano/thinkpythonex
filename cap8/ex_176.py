#NATO Phonetic Alphabet
def natoAlphabetSentenceConvert(word):
    dictionary={"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot",\
            "G":"Golf","H":"Hotel","I":"India","J":"Juliet","K":"Kilo","L":"Lima",\
            "M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo",\
            "S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"Xray","Y":"Yankee","Z":"Zulu"}
    if word=="":
        return ""
    word=word.upper()
    ch=dictionary[word[0]]
    word_tail=word[1:len(word)]
    return ch+" "+natoAlphabetSentenceConvert(word_tail)

def main():
    parola=input("Inserisci parola da convertire con l'alfabeto NATO: ")
    print(natoAlphabetSentenceConvert(parola))

if __name__ == '__main__':
    main()


