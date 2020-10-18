#Fattori primi

"""
Initialize factor to 2
While factor is less than or equal to n do
If n is evenly divisible by factor then
Conclude that factor is a factor of n
Divide n by factor using floor division
Else
Increase factor by 1
"""

n=int(input("INserisci intero(maggiore di 1):"))
fattore=2 #da algoritmo

if n>=2:
    while fattore<=n:
        if n%fattore==0:
            print("Fattore=",fattore)
            n=n//fattore
        else:
            fattore+=1
else:
    print("Hai inserito un numero minore di 2.")