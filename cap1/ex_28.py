#indice di vento gelido

temp=float(input("INserisci temperatura in C°: "))
vel_vento=float(input("Inserisci velocità vento in km/h: "))

WCI=13.12+0.6215*temp-11.37*vel_vento**(0.16)+0.3965*temp*(vel_vento**(0.16))

print("L'indice di vento gelido WCI è: %.2f"% WCI)