#Richter

magnitudo=float(input("Inserisci valore magnitudo:"))

if magnitudo<2.0:
    scala="Micro"
elif 2.0<magnitudo<3.0:
    scala="Very Minor"
elif 3.0<=magnitudo<4.0:
    scala="Minor"
elif 4.0<=magnitudo<5.0:
    scala="Light"
elif 5.0<=magnitudo<6.0:
    scala="Moderate"
elif 6.0<=magnitudo<7.0:
    scala="Strong"
elif 7.0<=magnitudo<8.0:
    scala="Major"
elif 8.0<=magnitudo<10.0:
    scala="great"
elif magnitudo>=10.0:
    scala="Meteoric"

print("Grado scala Richter: ", scala)

