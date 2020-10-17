#cambio monete atm

TOONIE=200
LOONIE=100
QUARTER=25
NICKEL=5
PENNY=1

cents=int(input("Inserire valore del resto in centesimi"))
print("Suddivisione monete:")
#Toonie(2 dollari)

print("",cents//TOONIE, " toonie")
cents=cents%TOONIE

#Loonie(1 dollaro)

print("",cents//LOONIE, " loonie")
cents=cents%LOONIE

#Quarter

print("",cents//QUARTER, " quarter")
cents=cents%QUARTER

#Nickel

print("",cents//NICKEL, " nickel")
cents=cents%NICKEL

#Cents

print("",cents, " cents")


