#calcolo giorno della settimana in cui cade capodanno a un certo anno

import math

year=int(input("Inserisci anno: "))

day_of_the_week = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7

if day_of_the_week==0:
    giornoCapodanno="Domenica"
elif day_of_the_week==1:
    giornoCapodanno="Lunedì"
elif day_of_the_week==2:
    giornoCapodanno="Martedì"
elif day_of_the_week==3:
    giornoCapodanno="Mercoledì"
elif day_of_the_week==4:
    giornoCapodanno="Giovedì"
elif day_of_the_week==5:
    giornoCapodanno="Venerdì"
elif day_of_the_week==6:
    giornoCapodanno="Sabato"

print("Nel",year,"l'1 Gennaio capita di",giornoCapodanno)
