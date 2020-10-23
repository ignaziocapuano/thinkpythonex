#reverse sorted order


list=[]
num=int(input("Inserisci primo elemento della List: "))
while num!=0:
    list.append(num)
    num = int(input("Inserisci numero da aggiungere alla List(0 per interrompere): "))

list.sort(reverse=True)

for i in range(len(list)):
    print(list[i])