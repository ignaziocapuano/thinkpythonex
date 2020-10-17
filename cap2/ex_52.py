#punteggi esami da lettere a numero

voto=input("Inserisci voto in lettera tra(A B C D F con + o - (tranne per F)")

if voto== "A":
    votoNum=4.0
elif voto== "A+":
    votoNum = 4.0
elif voto == "A-":
    votoNum = 3.7
elif voto == "B+":
    votoNum = 3.3
elif voto == "B":
    votoNum = 3.0
elif voto == "B-":
    votoNum = 2.7
elif voto == "C+":
    votoNum = 2.3
elif voto == "C":
    votoNum = 2.0
elif voto == "C-":
    votoNum = 1.7
elif voto == "D+":
    votoNum = 1.3
elif voto == "D":
    votoNum = 1.0
elif voto == "F":
    votoNum = 0
else:
    votoNum=-1

if votoNum==-1:
    print("Voto inserito non valido")
else:
    print("Voto in numeri=",votoNum)
