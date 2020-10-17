#somma cifre numero intero

num=int(input("Inserisci numero a 4 cifre: "))

#Calcolo le cifre con divisione intera e modulo come negli esercizi precedenti

x1000=num//1000
num=num%1000
x100=num//100
num=num%100
x10=num//10
num=num%10
x1=num

#C'è il problema che è possibile inserire piu di 4 cifre, ma eviterò di risoverlo in quanto la soluzione concerne capitoli successivi

print(x1000,"+",x100,"+",x10,"+",x1,"=",x1000+x100+x10+x1)

