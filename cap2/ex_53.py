#Voto da numeri a lettere

votoNum=float(input("Inserisci voto in punteggio>0.0:"))

if votoNum>=4.0:
    voto="A+"
elif 3.7<=votoNum<4.0:
    voto="A"
elif 3.3<=votoNum<3.7:
    voto="A-"
elif 3.0<=votoNum<3.3:
    voto="B+"
elif 2.7<=votoNum<3.0:
    voto="B"
elif 2.3<=votoNum<2.7:
    voto="B-"
elif 2.0<=votoNum<2.3:
    voto="C+"
elif 1.7<=votoNum<2.0:
    voto="C"
elif 1.3<=votoNum<1.7:
    voto="C-"
elif 1.0<=votoNum<1.3:
    voto="D+"
elif 0<=votoNum<1.0:
    voto="D"
elif votoNum==0:
    voto="F"
else:
    voto="Non valido"

print("Il voto in lettere è: ",voto)
