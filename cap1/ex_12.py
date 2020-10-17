import math

print("Inserisci le coordinate del primo punto:")
x1=float(input("t1="))
x1=math.radians(x1)
y1=float(input("g1="))
y1=math.radians(y1)
x2=float(input("t2="))
x2=math.radians(x2)
y2=float(input("g2="))
y2=math.radians(y2)
distanza=6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("La distanza tra i due punti è km", distanza)