#Line of Best Fit

"""
Inserisci serie di punti e approssima retta con questi valori
m=(sum(xy)-(sum(x)*sum(y))/n)/(sum(x**2)-(sum(x))**2/n
b=avg(y)-m*avg(x)
"""

#Input dati
x_list=[]
y_list=[]

for i in range(2):  #Almeno due punti per una retta
    x=float(input("Inserisci coordinata X:"))
    y=float(input("Inserisci coordinata Y:"))
    x_list.append(x)
    y_list.append(y)
x=input(("Inserisci coordinata X(Vuoto per fermare)"))
while x!="":
    y = float(input("Inserisci coordinata Y:"))
    x_list.append(float(x))
    y_list.append(y)
    x = input(("Inserisci coordinata X(Vuoto per fermare)"))
#Funzione
n=len(x_list)
somma_x=0
for i in range(n):
    somma_x+=x_list[i]
somma_y=0
for i in range(n):
    somma_y+=y_list[i]
somma_x_square=0
for i in range(n):
    somma_x_square+=x_list[i]**2
somma_xy=0
for i in range(n):
    somma_xy+=x_list[i]*y_list[i]
avg_x=somma_x/n
avg_y=somma_y/n
m=(somma_xy-(somma_x*somma_y)/n)/(somma_x_square-(somma_x)**2/n)
b=avg_y-m*avg_x

print("y="+"%2d"% m+"x"+"%+d" % b)
