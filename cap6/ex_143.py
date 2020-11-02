#Anagrams

string1=input("Inserisci prima parola: ")
string2=input("Inserisci seconda parola: ")
if len(string1)!=len(string2):
    print("Parole di lunghezza diversa")
    quit()
elif string1==string2:
    print("Parole uguali")
count1={}
count2={}
for i in range(len(string1)):
    if string1[i] in count1:
        count1[string1[i]]+=1
    else:
        count1[string1[i]]=1
for i in range(len(string2)):
    if string2[i] in count2:
        count2[string2[i]]+=1
    else:
        count2[string2[i]]=1
isAnagram=True
for key in count1:
    if key in count2.keys() or count1[key]==count2[key]:
        pass
    else:
        isAnagram=False

if isAnagram:
    print("Le parole sono anagrammi")

