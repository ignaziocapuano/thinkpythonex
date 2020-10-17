"""
day old bread
"""

prezzoPane=3.49
scontoPaneVecchio=60/100

n=int(input("Numero di panini vecchi acquistati:"))

prezzoTOTINT=n*prezzoPane
scontoTOT=prezzoTOTINT*scontoPaneVecchio
prezzoFIN=prezzoTOTINT-scontoTOT

print("PREZZO REGOLARE","%6.2f" % prezzoTOTINT)
print("SCONTO 60%     ","%6.2f" % scontoTOT)
print("---------------")
print("PREZZO FINALE  ","%6.2f" % prezzoFIN)

