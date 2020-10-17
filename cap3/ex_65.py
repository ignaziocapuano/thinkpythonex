#tabella conversioen temperatura

print("TEMPERATURA")
print("°C\t°F")

tempC=0
for tempC in range(0,110,10):
    tempF=(tempC*9/5)+32
    print(tempC,"\t", tempF)
