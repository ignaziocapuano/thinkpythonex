#Unique Characters


string=input("Inserisci frase")

dictionary={}

for i in range(len(string)):
    if string[i] in dictionary:
        dictionary[string[i]]+=1
    else:
        dictionary[string[i]]=1
count=0
for keys in dictionary:
    if dictionary[keys]>0:
        count+=1
print("Ci sono", count,"Caratteri unici")