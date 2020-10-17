#unita di tempo2


secondi=int(input("Inserisci numero di secondi:"))

giorni=secondi//(3600*24)
secondi=secondi%(3600*24)
ore=secondi//3600
secondi=secondi%3600
minuti=secondi//60
secondi=secondi%60

print("DD/HH/MM/SS")
print("%02d"% giorni+"/%02d"% ore+"/%02d"% minuti+ "/%02d"% secondi)


