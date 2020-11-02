#Total the Values

"""
Leggi da input una serie di valori(con terminatore il carattere nullo).
Alla fine stampa la somma. (0.0 se il primo carattere inserito dall'utente è vuoto)
"""

def readAndSum():
    n=input("Inserisci numero(vuoto per terminare:")
    if n=="":
        return 0.0
    else:
        return float(n)+readAndSum()

def main():
    total=readAndSum()
    print(total)

if __name__ == '__main__':
    main()

