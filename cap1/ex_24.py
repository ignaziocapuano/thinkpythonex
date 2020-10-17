#unita di tempo

giorni=int(input("Inserisci numero di giorni:"))
ore=int(input("Inserisci numero di ore:"))
minuti=int(input("Inserisci numero di minuti:))
secondi=int(input("Inserisci numero di secondi:))

secondi=secondi+minuti*60+ore*3600+giorni*3600*24

print("In secondi:"secondi)


