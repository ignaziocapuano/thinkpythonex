#MASSIMO comune divisore

"""
interi n m
divisore d
"""

n=int(input("inserisci primo numero"))
m=int(input("inserisci secondo numero"))

d=min(n,m)

while n%d!=0 or m%d!=0:
    d-=1

print("Il massimo comune divisore tra",n,"e",m,"è",d)