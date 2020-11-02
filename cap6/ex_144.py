#Anagrams Again

string1=input("Inserisci prima parola: ")
string2=input("Inserisci seconda parola: ")
string1=string1.lower()
string2=string2.lower()
if string1==string2:
    print("Frasi uguali")
count1={}
count2={}
for i in range(len(string1)):
    if string1[i]==" ":
        pass
    if string1[i] in count1:
        count1[string1[i]]+=1
    else:
        count1[string1[i]]=1
for i in range(len(string2)):
    if string2[i]==" ":
        pass
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
    print("Le frasi sono anagrammi")

