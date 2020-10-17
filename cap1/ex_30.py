#Conversione Pressione

pressKP=int(input("Inserisci pressione in KiloPascal:"))

pressPPSI=pressKP*6.895
pressMMOM=pressKP*7.501
pressATM=pressKP/101

print("Conversioni di",pressKP,"KiloPascal:")
print("%.2f"% pressPPSI,"ppsi")
print("%.2f"%pressMMOM,"MMOM")
print("%.2f"%pressATM, "ATM")