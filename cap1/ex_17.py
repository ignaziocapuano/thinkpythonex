#cerchi e sfere

CAPACITY_WATER=4.186
COSTO_CORRENTE_KWH=8.9

mass=float(input("Inserire massa in grammi:"))
temp_delta=float(input("Inserire variazione di temperaturea "))

q_joule=mass*CAPACITY_WATER*temp_delta
#in joule

print("Energia necessaria in Joule:", q_joule)

#trasformo in kwh

q_kwh=q_joule/(3.6*10**6)

consumo=COSTO_CORRENTE_KWH*q_kwh

#sta volta accorcio l'output dei float con %.2f

print("Costo consumo elettrico in cents: %.2f" % consumo)


