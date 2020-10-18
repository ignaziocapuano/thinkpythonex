#approssima pigreco
"""
Mostrare a schermo 15 approssimazioni di pigreco con un ciclo while usando la serie
Pi=3+4/(2*3*4)+4/(4*5*6)....
"""
pie=3
N_APPROSSIMAZIONI=15

print("1 Approssimazione Pigreco = 3")

for i in range(1,N_APPROSSIMAZIONI+1):
    if i%2==0:
        #print(pie, "-", "4/(",2*i,"*",2*i + 1,"*",2*i + 2,")")
        pie = pie - (4 / ((2*i) * (2*i + 1) * (2*i + 2)))
    else:
        #print(pie, "+", "4/(",2*i,"*",2*i + 1,"*",2*i + 2,")")
        pie = pie + (4 / ((2*i) * (2*i + 1) * (2*i + 2)))
    print(i+1,"Approssimazione Pigreco =",pie)

