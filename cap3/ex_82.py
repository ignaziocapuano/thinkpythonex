#decimale>binario

n=int(input("Inserisci numero da convertire in binario:"))

risultato=""

while n!=0:
    r=n%2
    risultato=str(r)+risultato
    n=n//2

print("In binario=",risultato)